#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Train Qwen3-4B OPSD models on selected multilingual translated
# datasets individually.
#
# Output structure:
#   ./multilingual_models_new_additional/bn/
#   ./multilingual_models_new_additional/sw/
#   ...
# ============================================================

# ISO 639-1 lowercase language codes
LANGS=(
  "bn"  # Bengali
  "sw"  # Swahili
  "te"  # Telugu
  "th"  # Thai
  "zh"  # Chinese
  "es"  # Spanish
  "ru"  # Russian
  "ja"  # Japanese
)

DATA_DIR="./translated_opsd_3000"
BASE_OUTPUT_DIR="./multilingual_models_new_additional"
MODEL_NAME="Qwen/Qwen3-4B"

# If you run multiple scripts on the same machine, change this port.
PORT=12970

# GPUs used by accelerate.
CUDA_DEVICES="0,1,2,3"
NUM_PROCESSES=4

# Training hyperparameters
LEARNING_RATE="5e-6"
MAX_GRAD_NORM="0.1"
PER_DEVICE_TRAIN_BATCH_SIZE=4
GRADIENT_ACCUMULATION_STEPS=2
NUM_TRAIN_EPOCHS=10
MAX_STEPS=100
SAVE_STEPS=5
LOGGING_STEPS=2

MAX_COMPLETION_LENGTH=2048
MAX_LENGTH=20000

# vLLM colocate settings
VLLM_GPU_MEMORY_UTILIZATION=0.6
VLLM_TENSOR_PARALLEL_SIZE=1

# LoRA settings
LORA_R=64
LORA_ALPHA=128

# Decoding settings
TEMPERATURE=1.1
TOP_P=0.95
TOP_K=20

# OPSD settings
LMBDA=1
JSD_TOKEN_CLIP=0.05

WANDB_PROJECT="Multilingual-OPSD"

mkdir -p "${BASE_OUTPUT_DIR}"

for lang in "${LANGS[@]}"; do
    LANG_UPPER="$(echo "$lang" | tr '[:lower:]' '[:upper:]')"

    DATA_PATH="${DATA_DIR}/translated_3000_${lang}.json"
    OUTPUT_DIR="${BASE_OUTPUT_DIR}/${lang}/"
    RUN_CONFIG="qwen3_4b_${lang}_opsd_3000_max${MAX_COMPLETION_LENGTH}"

    if [[ ! -f "$DATA_PATH" ]]; then
        echo "[ERROR] Missing data file: $DATA_PATH"
        exit 1
    fi

    echo "============================================================"
    echo "Training multilingual OPSD model"
    echo "Language                 : ${LANG_UPPER}"
    echo "Language code            : ${lang}"
    echo "Data                     : ${DATA_PATH}"
    echo "Output                   : ${OUTPUT_DIR}"
    echo "Run config               : ${RUN_CONFIG}"
    echo "Model                    : ${MODEL_NAME}"
    echo "CUDA devices             : ${CUDA_DEVICES}"
    echo "Num processes            : ${NUM_PROCESSES}"
    echo "Port                     : ${PORT}"
    echo "Learning rate            : ${LEARNING_RATE}"
    echo "Batch size / device      : ${PER_DEVICE_TRAIN_BATCH_SIZE}"
    echo "Grad accumulation        : ${GRADIENT_ACCUMULATION_STEPS}"
    echo "Max steps                : ${MAX_STEPS}"
    echo "Save steps               : ${SAVE_STEPS}"
    echo "Max completion length    : ${MAX_COMPLETION_LENGTH}"
    echo "Max length               : ${MAX_LENGTH}"
    echo "vLLM GPU utilization     : ${VLLM_GPU_MEMORY_UTILIZATION}"
    echo "============================================================"

    CUDA_VISIBLE_DEVICES="${CUDA_DEVICES}" accelerate launch \
        --config_file accelerate.yaml \
        --num_processes "${NUM_PROCESSES}" \
        --gradient_accumulation_steps "${GRADIENT_ACCUMULATION_STEPS}" \
        --main_process_port "${PORT}" \
        multilingual_opsd_train.py \
        --train_language "${LANG_UPPER}" \
        --translated_data_path "${DATA_PATH}" \
        --model_name_or_path "${MODEL_NAME}" \
        --learning_rate "${LEARNING_RATE}" \
        --max_grad_norm "${MAX_GRAD_NORM}" \
        --per_device_train_batch_size "${PER_DEVICE_TRAIN_BATCH_SIZE}" \
        --gradient_checkpointing \
        --gradient_accumulation_steps "${GRADIENT_ACCUMULATION_STEPS}" \
        --output_dir "${OUTPUT_DIR}" \
        --run_config "${RUN_CONFIG}" \
        --num_train_epochs "${NUM_TRAIN_EPOCHS}" \
        --max_completion_length "${MAX_COMPLETION_LENGTH}" \
        --max_steps "${MAX_STEPS}" \
        --save_steps "${SAVE_STEPS}" \
        --logging_steps "${LOGGING_STEPS}" \
        --attn_implementation flash_attention_2 \
        --torch_dtype bfloat16 \
        --max_length "${MAX_LENGTH}" \
        --beta 0 \
        --use_vllm \
        --vllm_mode colocate \
        --vllm_gpu_memory_utilization "${VLLM_GPU_MEMORY_UTILIZATION}" \
        --vllm_tensor_parallel_size "${VLLM_TENSOR_PARALLEL_SIZE}" \
        --use_peft \
        --lora_r "${LORA_R}" \
        --lora_alpha "${LORA_ALPHA}" \
        --lora_target_modules q_proj k_proj v_proj o_proj gate_proj up_proj down_proj \
        --temperature "${TEMPERATURE}" \
        --top_p "${TOP_P}" \
        --top_k "${TOP_K}" \
        --lmbda "${LMBDA}" \
        --fixed_teacher \
        --student_enable_thinking \
        --jsd_token_clip "${JSD_TOKEN_CLIP}" \
        --wandb_project "${WANDB_PROJECT}"

    echo "[OK] Finished ${LANG_UPPER}"
    echo
done

echo "All selected multilingual OPSD runs finished."