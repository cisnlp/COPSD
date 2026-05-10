LANGUAGE_CONFIG = {
    "EN": {
        "student_instruction": (
            "Please reason step by step, and put your final answer within \\boxed{}."
        ),
        "think_prefix": (
            "By request, I will start thinking in English."
        ),
        "reason_first_prompt": (
            "The English reference solution above arrives at the correct answer. "
            "Please analyze this solution and explain the key reasoning steps and problem-solving strategies employed. "
            "Do NOT use <think> tags. Do NOT derive your own solution yet. "
            "Simply analyze and explain the reference solution provided above."
        ),
        "transition_prompt": (
            "After reading the English reference solution above, make sure you truly understand the logic behind each step—"
            "do not copy it or merely paraphrase it. "
            "Now, using your own words and independent reasoning, solve the original problem in English. "
            "Think step by step, try different approaches, and do not hesitate to backtrack or reconsider if something does not work:"
        ),
        "teacher_final_instruction": (
            "Please reason step by step in English, and put your final answer within \\boxed{}."
        ),
        "labels": {
            "problem_target": "Problem",
            "problem_english": "English translation of the problem",
            "solution_english": "Correct English reference solution",
            "ref_begin": "=== Reference Solution Begin ===",
            "ref_end": "=== Reference Solution End ===",
        },
    },

    "DE": {
        "student_instruction": (
            "Bitte denke Schritt für Schritt und setze deine endgültige Antwort in \\boxed{}."
        ),
        "think_prefix": (
            "Auf Anfrage werde ich anfangen, in Deutsch zu denken."
        ),
        "reason_first_prompt": (
            "Die englische Referenzlösung oben führt zur richtigen Antwort. "
            "Bitte analysiere diese Lösung und erkläre die wichtigsten Denkschritte und Lösungsstrategien. "
            "Verwende KEINE <think>-Tags. Leite noch keine eigene Lösung her. "
            "Analysiere und erkläre nur die bereitgestellte Referenzlösung."
        ),
        "transition_prompt": (
            "Nachdem du die englische Referenzlösung oben gelesen hast, stelle sicher, dass du die Logik hinter jedem Schritt wirklich verstanden hast—"
            "kopiere sie nicht und formuliere sie nicht nur um. "
            "Löse nun die ursprüngliche Aufgabe auf Deutsch mit deinen eigenen Worten und durch eigenständiges Denken. "
            "Denke Schritt für Schritt, probiere verschiedene Ansätze aus und zögere nicht, zurückzugehen oder neu zu überlegen, wenn etwas nicht funktioniert:"
        ),
        "teacher_final_instruction": (
            "Bitte denke Schritt für Schritt auf Deutsch und setze deine endgültige Antwort in \\boxed{}."
        ),
        "labels": {
            "problem_target": "Aufgabe",
            "problem_english": "Englische Übersetzung der Aufgabe",
            "solution_english": "Korrekte englische Referenzlösung",
            "ref_begin": "=== Beginn der Referenzlösung ===",
            "ref_end": "=== Ende der Referenzlösung ===",
        },
    },

    "ES": {
        "student_instruction": (
            "Por favor, razona paso a paso y coloca tu respuesta final dentro de \\boxed{}."
        ),
        "think_prefix": (
            "A petición, empezaré a pensar en español."
        ),
        "reason_first_prompt": (
            "La solución de referencia en inglés de arriba llega a la respuesta correcta. "
            "Analiza esta solución y explica los pasos clave de razonamiento y las estrategias utilizadas. "
            "NO uses etiquetas <think>. NO derives todavía tu propia solución. "
            "Solo analiza y explica la solución de referencia proporcionada."
        ),
        "transition_prompt": (
            "Después de leer la solución de referencia en inglés anterior, asegúrate de comprender realmente la lógica detrás de cada paso—"
            "no la copies ni te limites a parafrasearla. "
            "Ahora, usando tus propias palabras y un razonamiento independiente, resuelve el problema original en español. "
            "Piensa paso a paso, prueba distintos enfoques y no dudes en retroceder o reconsiderar si algo no funciona:"
        ),
        "teacher_final_instruction": (
            "Por favor, razona paso a paso en español y coloca tu respuesta final dentro de \\boxed{}."
        ),
        "labels": {
            "problem_target": "Problema",
            "problem_english": "Traducción al inglés del problema",
            "solution_english": "Solución de referencia correcta en inglés",
            "ref_begin": "=== Inicio de la solución de referencia ===",
            "ref_end": "=== Fin de la solución de referencia ===",
        },
    },

    "FR": {
        "student_instruction": (
            "Veuillez raisonner étape par étape et mettre votre réponse finale dans \\boxed{}."
        ),
        "think_prefix": (
            "Sur demande, je commencerai à penser en français."
        ),
        "reason_first_prompt": (
            "La solution de référence en anglais ci-dessus aboutit à la bonne réponse. "
            "Veuillez analyser cette solution et expliquer les étapes de raisonnement clés ainsi que les stratégies employées. "
            "N'utilisez PAS de balises <think>. Ne dérivez pas encore votre propre solution. "
            "Analysez et expliquez simplement la solution de référence fournie."
        ),
        "transition_prompt": (
            "Après avoir lu la solution de référence en anglais ci-dessus, assurez-vous de bien comprendre la logique de chaque étape—"
            "ne la copiez pas et ne vous contentez pas de la paraphraser. "
            "Maintenant, avec vos propres mots et un raisonnement indépendant, résolvez le problème original en français. "
            "Raisonnez étape par étape, essayez différentes approches et n'hésitez pas à revenir en arrière ou à reconsidérer votre raisonnement si quelque chose ne fonctionne pas:"
        ),
        "teacher_final_instruction": (
            "Veuillez raisonner étape par étape en français et mettre votre réponse finale dans \\boxed{}."
        ),
        "labels": {
            "problem_target": "Problème",
            "problem_english": "Traduction anglaise du problème",
            "solution_english": "Solution de référence correcte en anglais",
            "ref_begin": "=== Début de la solution de référence ===",
            "ref_end": "=== Fin de la solution de référence ===",
        },
    },

    "JA": {
        "student_instruction": (
            "段階的に考え、最終的な答えを \\boxed{} の中に入れてください。"
        ),
        "think_prefix": (
            "要望があれば、日本語で考え始めます。"
        ),
        "reason_first_prompt": (
            "上の英語の参照解答は正しい答えに到達しています。"
            "この解答を分析し、重要な推論の流れと解法の方針を説明してください。"
            "<think> タグは使わないでください。まだ自分の解法を導かないでください。"
            "与えられた参照解答を分析して説明するだけにしてください。"
        ),
        "transition_prompt": (
            "上の英語の参照解答を読んだあと、各ステップの背後にある論理を本当に理解していることを確認してください。"
            "それをコピーしたり、単に言い換えたりしてはいけません。 "
            "次に、自分自身の言葉と独立した推論を用いて、元の問題を日本語で解いてください。 "
            "段階的に考え、複数の方法を試し、うまくいかない場合は戻って考え直すことをためらわないでください:"
        ),
        "teacher_final_instruction": (
            "日本語で段階的に考え、最終的な答えを \\boxed{} の中に入れてください。"
        ),
        "labels": {
            "problem_target": "問題",
            "problem_english": "問題の英語版",
            "solution_english": "正しい英語の参照解答",
            "ref_begin": "=== 参照解答の開始 ===",
            "ref_end": "=== 参照解答の終了 ===",
        },
    },

    "ZH": {
        "student_instruction": (
            "请一步一步推理，并将最终答案放在 \\boxed{} 中。"
        ),
        "think_prefix": (
            "应要求，我将开始用中文思考。"
        ),
        "reason_first_prompt": (
            "上面的英文参考解答得出了正确答案。"
            "请分析这份解答，并说明其中关键的推理步骤和解题策略。"
            "不要使用 <think> 标签。暂时不要自己重新求解。"
            "只需分析并解释上面提供的参考解答。"
        ),
        "transition_prompt": (
            "在阅读上面的英文参考解答之后，请确保你真正理解了每一步背后的逻辑——"
            "不要复制它，也不要只是改写它。 "
            "现在，请用你自己的语言和独立推理，用中文解决原始问题。 "
            "请一步一步思考，尝试不同的方法；如果某个思路行不通，也不要犹豫返回并重新思考："
        ),
        "teacher_final_instruction": (
            "请用中文一步一步推理，并将最终答案放在 \\boxed{} 中。"
        ),
        "labels": {
            "problem_target": "题目",
            "problem_english": "题目的英文版本",
            "solution_english": "正确的英文参考解答",
            "ref_begin": "=== 参考解答开始 ===",
            "ref_end": "=== 参考解答结束 ===",
        },
    },

    "RU": {
        "student_instruction": (
            "Пожалуйста, рассуждайте шаг за шагом и поместите окончательный ответ в \\boxed{}."
        ),
        "think_prefix": (
            "По запросу я начну думать на русском."
        ),
        "reason_first_prompt": (
            "Англоязычное эталонное решение выше приводит к правильному ответу. "
            "Пожалуйста, проанализируйте это решение и объясните ключевые шаги рассуждения и использованные стратегии. "
            "НЕ используйте теги <think>. Пока не выводите собственное решение. "
            "Просто проанализируйте и объясните данное эталонное решение."
        ),
        "transition_prompt": (
            "После прочтения приведенного выше эталонного решения на английском убедитесь, что вы действительно понимаете логику каждого шага—"
            "не копируйте его и не ограничивайтесь простым пересказом. "
            "Теперь, используя собственные слова и самостоятельное рассуждение, решите исходную задачу по-русски. "
            "Рассуждайте шаг за шагом, пробуйте разные подходы и не бойтесь вернуться назад или пересмотреть ход решения, если что-то не работает:"
        ),
        "teacher_final_instruction": (
            "Пожалуйста, рассуждайте шаг за шагом на русском и поместите окончательный ответ в \\boxed{}."
        ),
        "labels": {
            "problem_target": "Задача",
            "problem_english": "Английский перевод задачи",
            "solution_english": "Правильное эталонное решение на английском",
            "ref_begin": "=== Начало эталонного решения ===",
            "ref_end": "=== Конец эталонного решения ===",
        },
    },

    "SW": {
        "student_instruction": (
            "Tafadhali fikiri hatua kwa hatua, na uweke jibu lako la mwisho ndani ya \\boxed{}."
        ),
        "think_prefix": (
            "Kwa ombi, nitaanza kufikiria kwa Kiswahili."
        ),
        "reason_first_prompt": (
            "Suluhisho la rejeleo la Kiingereza hapo juu linafikia jibu sahihi. "
            "Tafadhali chambua suluhisho hili na ueleze hatua kuu za hoja pamoja na mikakati ya utatuzi iliyotumika. "
            "USITUMIE alama za <think>. Usitoe suluhisho lako mwenyewe bado. "
            "Chambua na eleza tu suluhisho la rejeleo ulilopewa."
        ),
        "transition_prompt": (
            "Baada ya kusoma suluhisho la rejeleo la Kiingereza hapo juu, hakikisha umeelewa kweli mantiki ya kila hatua—"
            "usilinakili wala kulifafanua upya tu. "
            "Sasa, kwa kutumia maneno yako mwenyewe na hoja huru, tatua swali la asili kwa Kiswahili. "
            "Fikiri hatua kwa hatua, jaribu mbinu tofauti, na usiogope kurudi nyuma au kufikiria upya ikiwa jambo fulani halifanyi kazi:"
        ),
        "teacher_final_instruction": (
            "Tafadhali fikiri hatua kwa hatua kwa Kiswahili, na uweke jibu lako la mwisho ndani ya \\boxed{}."
        ),
        "labels": {
            "problem_target": "Swali",
            "problem_english": "Tafsiri ya Kiingereza ya swali",
            "solution_english": "Suluhisho sahihi la rejeleo kwa Kiingereza",
            "ref_begin": "=== Mwanzo wa Suluhisho la Rejeleo ===",
            "ref_end": "=== Mwisho wa Suluhisho la Rejeleo ===",
        },
    },

    "BN": {
        "student_instruction": (
            "দয়া করে ধাপে ধাপে ভাবুন এবং আপনার চূড়ান্ত উত্তর \\boxed{} এর মধ্যে দিন।"
        ),
        "think_prefix": (
            "অনুরোধ করলে, আমি বাংলায় চিন্তা করা শুরু করব।"
        ),
        "reason_first_prompt": (
            "উপরের ইংরেজি রেফারেন্স সমাধানটি সঠিক উত্তরে পৌঁছেছে। "
            "দয়া করে এই সমাধানটি বিশ্লেষণ করুন এবং মূল যুক্তির ধাপ ও ব্যবহৃত সমাধান-কৌশল ব্যাখ্যা করুন। "
            "<think> ট্যাগ ব্যবহার করবেন না। এখনই নিজের সমাধান বের করবেন না। "
            "শুধু দেওয়া রেফারেন্স সমাধানটি বিশ্লেষণ ও ব্যাখ্যা করুন।"
        ),
        "transition_prompt": (
            "উপরের ইংরেজি রেফারেন্স সমাধানটি পড়ার পর নিশ্চিত করুন যে আপনি প্রতিটি ধাপের পেছনের যুক্তি সত্যিই বুঝেছেন—"
            "এটি কপি বা কেবল পুনর্লিখন করবেন না। "
            "এখন আপনার নিজের ভাষায় এবং স্বাধীন যুক্তির মাধ্যমে মূল সমস্যাটি বাংলায় সমাধান করুন। "
            "ধাপে ধাপে ভাবুন, বিভিন্ন পদ্ধতি চেষ্টা করুন, এবং কোনো কিছু কাজ না করলে ফিরে গিয়ে আবার বিবেচনা করতে দ্বিধা করবেন না:"
        ),
        "teacher_final_instruction": (
            "দয়া করে বাংলায় ধাপে ধাপে ভাবুন এবং আপনার চূড়ান্ত উত্তর \\boxed{} এর মধ্যে দিন।"
        ),
        "labels": {
            "problem_target": "সমস্যা",
            "problem_english": "সমস্যার ইংরেজি সংস্করণ",
            "solution_english": "সঠিক ইংরেজি রেফারেন্স সমাধান",
            "ref_begin": "=== রেফারেন্স সমাধান শুরু ===",
            "ref_end": "=== রেফারেন্স সমাধান শেষ ===",
        },
    },

    "TE": {
        "student_instruction": (
            "దయచేసి దశలవారీగా ఆలోచించి, మీ చివరి సమాధానాన్ని \\boxed{} లో పెట్టండి."
        ),
        "think_prefix": (
            "అభ్యర్థన మేరకు, నేను తెలుగులో ఆలోచించడం ప్రారంభిస్తాను."
        ),
        "reason_first_prompt": (
            "పై ఉన్న ఆంగ్ల సూచనాత్మక పరిష్కారం సరైన సమాధానానికి చేరుకుంది. "
            "దయచేసి ఈ పరిష్కారాన్ని విశ్లేషించి, ముఖ్యమైన తార్కిక దశలను మరియు ఉపయోగించిన పరిష్కార వ్యూహాలను వివరించండి. "
            "<think> ట్యాగ్‌లను ఉపయోగించవద్దు. ఇప్పుడే మీ స్వంత పరిష్కారాన్ని రూపొందించవద్దు. "
            "ఇచ్చిన సూచనాత్మక పరిష్కారాన్ని మాత్రమే విశ్లేషించి వివరించండి."
        ),
        "transition_prompt": (
            "పై ఉన్న ఆంగ్ల సూచనాత్మక పరిష్కారాన్ని చదివిన తర్వాత, ప్రతి దశ వెనుక ఉన్న తర్కాన్ని మీరు నిజంగా అర్థం చేసుకున్నారని నిర్ధారించుకోండి—"
            "దాన్ని కాపీ చేయవద్దు లేదా కేవలం మరోలా చెప్పవద్దు. "
            "ఇప్పుడు మీ స్వంత మాటలతో మరియు స్వతంత్ర తర్కంతో అసలు ప్రశ్నను తెలుగులో పరిష్కరించండి. "
            "దశలవారీగా ఆలోచించండి, భిన్నమైన పద్ధతులను ప్రయత్నించండి, ఏదైనా పనిచేయకపోతే వెనక్కి వెళ్లి మళ్లీ ఆలోచించడానికి సంకోచించవద్దు:"
        ),
        "teacher_final_instruction": (
            "దయచేసి తెలుగులో దశలవారీగా ఆలోచించి, మీ చివరి సమాధానాన్ని \\boxed{} లో పెట్టండి."
        ),
        "labels": {
            "problem_target": "ప్రశ్న",
            "problem_english": "ప్రశ్న యొక్క ఆంగ్ల అనువాదం",
            "solution_english": "సరైన ఆంగ్ల సూచనాత్మక పరిష్కారం",
            "ref_begin": "=== సూచనాత్మక పరిష్కారం ప్రారంభం ===",
            "ref_end": "=== సూచనాత్మక పరిష్కారం ముగింపు ===",
        },
    },

    "TH": {
        "student_instruction": (
            "โปรดให้เหตุผลทีละขั้นตอน และใส่คำตอบสุดท้ายของคุณไว้ใน \\boxed{}"
        ),
        "think_prefix": (
            "ตามคำขอ ฉันจะเริ่มคิดเป็นภาษาไทย"
        ),
        "reason_first_prompt": (
            "วิธีทำอ้างอิงภาษาอังกฤษข้างต้นนำไปสู่คำตอบที่ถูกต้อง "
            "โปรดวิเคราะห์วิธีทำนี้และอธิบายขั้นตอนการให้เหตุผลที่สำคัญรวมถึงกลยุทธ์ที่ใช้แก้ปัญหา "
            "ห้ามใช้แท็ก <think> และยังไม่ต้องหาวิธีทำของตนเอง "
            "ให้วิเคราะห์และอธิบายเฉพาะวิธีทำอ้างอิงที่ให้มาเท่านั้น"
        ),
        "transition_prompt": (
            "หลังจากอ่านวิธีทำอ้างอิงภาษาอังกฤษข้างต้นแล้ว โปรดตรวจสอบให้แน่ใจว่าคุณเข้าใจตรรกะเบื้องหลังแต่ละขั้นตอนอย่างแท้จริง—"
            "อย่าคัดลอกหรือเพียงแค่ถอดความวิธีทำนั้น "
            "ตอนนี้ ให้ใช้ถ้อยคำของคุณเองและการให้เหตุผลอย่างอิสระเพื่อแก้โจทย์ต้นฉบับเป็นภาษาไทย "
            "คิดทีละขั้นตอน ลองใช้วิธีต่าง ๆ และอย่าลังเลที่จะย้อนกลับหรือพิจารณาใหม่หากบางอย่างใช้ไม่ได้ผล:"
        ),
        "teacher_final_instruction": (
            "โปรดให้เหตุผลทีละขั้นตอนเป็นภาษาไทย และใส่คำตอบสุดท้ายของคุณไว้ใน \\boxed{}"
        ),
        "labels": {
            "problem_target": "โจทย์",
            "problem_english": "คำแปลภาษาอังกฤษของโจทย์",
            "solution_english": "วิธีทำอ้างอิงภาษาอังกฤษที่ถูกต้อง",
            "ref_begin": "=== เริ่มวิธีทำอ้างอิง ===",
            "ref_end": "=== จบวิธีทำอ้างอิง ===",
        },
    },
}

AFRICAN_LANGUAGE_CONFIG = {
    # ============================================================
    # West Africa
    # ============================================================
    "EWE": {
        "student_instruction": (
            "Mesrɛ wo, bu akɔntaabu no afã afã, eye nàtsɔ wo ŋuɖoɖo mamlɛtɔ ade \\boxed{} me."
        ),
        "think_prefix": (
            "Le biabia me la, magɔme le susu wɔwɔ me le Eʋegbe me."
        ),
        "reason_first_prompt": (
            "Dɔwɔɖoɖo si le Eŋlisigbe me le etame la kplɔ yi ŋuɖoɖo nyuitɔ gbɔ. "
            "Mesrɛ wo, kpɔ dɔwɔɖoɖo sia me nyuie, eye nàɖe susu ƒe afɔ vevitɔwo kple mɔnu siwo wozã le kuxi la gɔmeɖeɖe me la me. "
            "Mègazã <think> dzesiwo o. Mègayi dzi wò ŋutɔ ƒe dɔwɔɖoɖo me haɖe o. "
            "Ðe dɔwɔɖoɖo si wona la gɔmeɖeɖe ko."
        ),
        "transition_prompt": (
            "Esi nèxlẽ Eŋlisigbe me dɔwɔɖoɖo si le etame la vɔ la, kpɔ egbɔ be èse susu si le afɔ ɖe sia ɖe megbe la gɔme nyuie—"
            "mègakɔpii alo agbugbɔ agblɔe abe ale si wogblɔe ene o. "
            "Fifia, zã wò ŋutɔ ƒe nya kple susu si nàwɔ le wò ŋutɔ me, eye nàɖe kuxi gɔmedzedze la le Eʋegbe me. "
            "Bu tame le afɔɖeɖe me, kpɔ mɔ vovovowo me, eye ne mɔ aɖe medze edzi o la, mèganɔ vɔ̃ na megbe trɔtrɔ alo susui yeye o:"
        ),
        "teacher_final_instruction": (
            "Mesrɛ wo, bu akɔntaabu no afã afã, eye nàtsɔ wo ŋuɖoɖo mamlɛtɔ ade \\boxed{} me."
        ),
        "labels": {
            "problem_target": "Kuxi",
            "problem_english": "Kuxi la ƒe Eŋlisigbe me gɔmeɖeɖe",
            "solution_english": "Eŋlisigbe me dɔwɔɖoɖo dzɔdzɔe",
            "ref_begin": "=== Dɔwɔɖoɖo ƒe gɔmedzedze ===",
            "ref_end": "=== Dɔwɔɖoɖo ƒe nuwuwu ===",
        },
    },

    "HAU": {
        "student_instruction": (
            "Da fatan ka yi tunani mataki-mataki, kuma ka sanya amsarka ta ƙarshe a cikin \\boxed{}."
        ),
        "think_prefix": (
            "Bisa buƙata, zan fara yin tunani da Hausa."
        ),
        "reason_first_prompt": (
            "Maganin misali na Turanci da ke sama ya kai ga amsa daidai. "
            "Da fatan ka binciki wannan magani ka bayyana muhimman matakan tunani da dabarun warware matsalar da aka yi amfani da su. "
            "Kada ka yi amfani da alamomin <think>. Kada ka fito da naka maganin tukuna. "
            "Ka bincika kuma ka bayyana maganin misalin da aka bayar kawai."
        ),
        "transition_prompt": (
            "Bayan ka karanta maganin misali na Turanci da ke sama, ka tabbatar cewa ka fahimci ainihin dalilin kowane mataki—"
            "kada ka kwafe shi ko ka sake faɗarsa da wasu kalmomi kawai. "
            "Yanzu, da kalmominka da tunaninka mai zaman kansa, ka warware matsalar asali da Hausa. "
            "Ka yi tunani mataki-mataki, ka gwada hanyoyi daban-daban, kuma kada ka ji tsoron komawa baya ko sake tunani idan wata hanya ba ta yi aiki ba:"
        ),
        "teacher_final_instruction": (
            "Da fatan ka yi tunani mataki-mataki da Hausa, kuma ka sanya amsarka ta ƙarshe a cikin \\boxed{}."
        ),
        "labels": {
            "problem_target": "Matsala",
            "problem_english": "Fassarar matsalar zuwa Turanci",
            "solution_english": "Madaidaicin maganin misali na Turanci",
            "ref_begin": "=== Farkon Maganin Misali ===",
            "ref_end": "=== Ƙarshen Maganin Misali ===",
        },
    },

    "IBO": {
        "student_instruction": (
            "Biko tụlee ya nzọụkwụ site na nzọụkwụ, ma tinye azịza ikpeazụ gị n'ime \\boxed{}."
        ),
        "think_prefix": (
            "Dị ka arịrịọ si dị, aga m amalite iche echiche n'asụsụ Igbo."
        ),
        "reason_first_prompt": (
            "Ngwọta ntụaka Bekee dị n'elu ruru azịza ziri ezi. "
            "Biko nyochaa ngwọta a ma kọwaa nzọụkwụ echiche ndị kacha mkpa na ụzọ e ji dozie nsogbu ahụ. "
            "Ejila akara <think>. Ewepụtala ngwọta nke gị ugbu a. "
            "Naanị nyochaa ma kọwaa ngwọta ntụaka e nyere."
        ),
        "transition_prompt": (
            "Mgbe ị gụsịrị ngwọta ntụaka Bekee dị n'elu, jide n'aka na ị ghọtara n'ezie echiche dị n'azụ nzọụkwụ ọ bụla—"
            "eṅomila ya ma ọ bụ kwuo ya ọzọ n'ụzọ ọzọ. "
            "Ugbu a, jiri okwu nke gị na echiche nke onwe gị dozie nsogbu mbụ ahụ n'asụsụ Igbo. "
            "Chee echiche nzọụkwụ site na nzọụkwụ, nwalee ụzọ dị iche iche, ma atụla egwu ịlaghachi azụ ma ọ bụ tụgharịa uche ọzọ ma ọ bụrụ na ihe adịghị arụ ọrụ:"
        ),
        "teacher_final_instruction": (
            "Biko tụlee ya nzọụkwụ site na nzọụkwụ n'asụsụ Igbo, ma tinye azịza ikpeazụ gị n'ime \\boxed{}."
        ),
        "labels": {
            "problem_target": "Nsogbu",
            "problem_english": "Nsụgharị Bekee nke nsogbu ahụ",
            "solution_english": "Ngwọta ntụaka Bekee ziri ezi",
            "ref_begin": "=== Mmalite Ngwọta Ntụaka ===",
            "ref_end": "=== Ngwụcha Ngwọta Ntụaka ===",
        },
    },

    "TWI": {
        "student_instruction": (
            "Yɛsrɛ wo, dwene ho anammɔn biara mu, na fa wo mmuae a etwa to no hyɛ \\boxed{} mu."
        ),
        "think_prefix": (
            "Sɛnea wɔabisa no, mɛfi ase adwene wɔ Twi mu."
        ),
        "reason_first_prompt": (
            "Borɔfo mu nhwɛsoɔ ano adwuma a ɛwɔ atifi hɔ no du mmuaeɛ a ɛyɛ nokware no ho. "
            "Yɛsrɛ wo, hwehwɛ ano adwuma yi mu na kyerɛkyerɛ adwene mu anammɔn titiriw ne akwan a wɔfaa so siesiee asɛmmisa no mu. "
            "Mfa <think> ahyɛnsodeɛ nni dwuma. Nnyaa wo ankasa ano adwuma no nkyerɛ ɛnnɛ ara. "
            "Hwehwɛ na kyerɛkyerɛ nhwɛsoɔ ano adwuma a wɔde ama no nko ara mu."
        ),
        "transition_prompt": (
            "Bere a woakenkan Borɔfo mu nhwɛsoɔ ano adwuma a ɛwɔ atifi hɔ no awie no, hwɛ sɛ wote adwene a ɛwɔ anammɔn biara akyi no ase yiye—"
            "nkɔpi no na nsan nka no wɔ nsɛmfua foforo mu kɛkɛ. "
            "Afei, fa wo ankasa nsɛmfua ne wo ankasa adwene siesie asɛmmisa a edi kan no wɔ Twi mu. "
            "Dwene ho anammɔn biara mu, sɔ akwan horow hwɛ, na sɛ biribi anyɛ adwuma a, nsuro sɛ wobɛsan akɔ akyi anaa wobɛsan adwene ho bio:"
        ),
        "teacher_final_instruction": (
            "Yɛsrɛ wo, dwene ho anammɔn biara mu wɔ Twi mu, na fa wo mmuae a etwa to no hyɛ \\boxed{} mu."
        ),
        "labels": {
            "problem_target": "Asɛmmisa",
            "problem_english": "Asɛmmisa no Borɔfo nkyerɛaseɛ",
            "solution_english": "Borɔfo mu nhwɛsoɔ ano adwuma a ɛyɛ nokware",
            "ref_begin": "=== Nhwɛsoɔ Ano Adwuma Ahyɛaseɛ ===",
            "ref_end": "=== Nhwɛsoɔ Ano Adwuma Awieeɛ ===",
        },
    },
    
    "VAI": {
        "student_instruction": (
            "ꕉ ꕘꕌꘋꕡ, ꔤ ꕞꕌ ꔳꘋ ꔳꘋ ꗏ ꖴꘋꗒ, ꔤ ꕒꕌꘋ ꔞꘋꗣ ꕉ ꗓ ꕉ ꕉꕌꘋꔕ ꗏ \\boxed{}."
        ),
        "think_prefix": (
            "ꗋꖺ ꕉ ꖏꕎꔀ ꗏ, ꔤ ꕘꕌ ꖴꘋꗒ ꕉ ꗓ ꔞꔀ ꗏ."
        ),
        "reason_first_prompt": (
            "ꔞꔀ ꗏ ꕉꕡꕌꔤ ꕧꕌꔤ ꗏ ꖴꘋꗒ ꕉ ꕒꕌꘋ ꔞꘋꗣ ꕉ ꗓ ꗋꖺ ꗏ. "
            "ꕉ ꕘꕌꘋꕡ, ꔤ ꕞꕌ ꖴꘋꗒ ꕉ ꗓ ꕉ ꗏ, ꔤ ꗓꕎ ꖴꘋꗒ ꕒꕌꘋ ꔳꘋ ꔳꘋ ꗏ ꗪ ꕢꕌꔳ ꕉ ꗏ ꔇꔀ ꕉ ꕎ. "
            "ꕉ ꕘꕌꘋꕡ, ꔤ ꕮ ꕞ <think> ꗏ. ꔤ ꕮ ꖴꘋꗒ ꔤ ꗓ ꕉꕌ ꗏ ꕒꕌꘋ ꔞꘋꗣ ꕉ ꕎ ꗦꗷ. "
            "ꖴꘋꗒ ꕉ ꔇꔀ ꔤ ꕸꖃ ꗏ ꗋꖺ ꔤ ꕞꕌ ꕉ ꗏ ꔇꔀ."
        ),
        "transition_prompt": (
            "ꔞꔀ ꗏ ꕉꕡꕌꔤ ꕧꕌꔤ ꗏ ꖴꘋꗒ ꕉ ꕞꕌ ꔞ ꗏ, ꔤ ꕢꕌꔳ ꕉ ꔳꘋ ꔳꘋ ꗏ ꖴꘋꗒ ꕢꕌ ꕉ ꗏ ꗋꖺ ꔤ ꗨꗡ ꕉ ꕎ—"
            "ꔤ ꕮ ꕉ ꕘꕌꔤ, ꔤ ꕮ ꕉ ꗓ ꗏ ꕞꕌ ꕉ ꗓ ꔇꔀ. "
            "ꘃꕯ, ꔤ ꗓ ꗏ ꕧꕌꔤ ꗪ ꔤ ꖴꘋꗒ ꔞꘋꗣ ꕉ ꗓ ꗏ, ꔤ ꕿꖃ ꕉ ꕞꕌ ꔞꔀ ꗏ. "
            "ꔤ ꕞꕌ ꔳꘋ ꔳꘋ ꗏ, ꔤ ꕢꕌꔳ ꗃꖺꘋ ꗏ ꕉ ꕎ, ꗪ ꔤ ꕮ ꕢꕌꘂ ꕉ ꗏ ꗓ ꔞ ꕉ ꕎ ꕉ ꕮ ꔇꔀ:"
        ),
        "teacher_final_instruction": (
            "ꕉ ꕘꕌꘋꕡ, ꔤ ꕞꕌ ꔳꘋ ꔳꘋ ꗏ ꔞꔀ ꗏ, ꔤ ꕒꕌꘋ ꔞꘋꗣ ꕉ ꗓ ꕉ ꕉꕌꘋꔕ ꗏ \\boxed{}."
        ),
        "labels": {
            "problem_target": "ꕿꖃ",
            "problem_english": "ꕿꖃ ꔞꔀ ꗏ ꗛꖺꕎ",
            "solution_english": "ꔞꔀ ꗏ ꖴꘋꗒ ꕉ ꗋꖺ",
            "ref_begin": "=== ꖴꘋꗒ ꕉ ꗓ ꗏ ꔳꘋ ===",
            "ref_end": "=== ꖴꘋꗒ ꕉ ꗓ ꗏ ꕉꕌꘋꔕ ===",
        },
    },

    "WOL": {
        "student_instruction": (
            "Ba beneen yoon, xalaatal ci ndànk-ndànk, te defal sa tontu mu mujj mi ci \\boxed{}."
        ),
        "think_prefix": (
            "Ci laaj bi, dinaa tàmbali xalaat ci Wolof."
        ),
        "reason_first_prompt": (
            "Saafara bu ñu jox ci àngale ci kaw ji agsi na ci tontu bu jub. "
            "Maa ngi la ñaan nga seet saafara bii, nga leeral jéego yi gën a am solo ci xalaat bi ak pexe yi ñu jëfandikoo ngir saafara jafe-jafe bi. "
            "Bul jëfandikoo màndarga <think>. Bul génne sa saafara boppam léegi. "
            "Seetal te leeralal rekk saafara bu ñu jox bi."
        ),
        "transition_prompt": (
            "Gannaaw boo jàngalee saafara bu ñu jox ci àngale ci kaw ji, wóorlu ne dëgg-dëgg nga xam xalaat bi nekk ci gannaaw jéego bu nekk—"
            "bul ko duppi, bul ko waxaat rekk ak beneen baat. "
            "Léegi, jëfandikool sa baati bopp ak sa xalaat bopp ngir saafara jafe-jafe bu njëkk bi ci Wolof. "
            "Xalaatal ci ndànk-ndànk, jéem yoon yu wuute, te bu dara doxul, bul ragal dellu gannaaw walla xalaat ci beneen yoon:"
        ),
        "teacher_final_instruction": (
            "Ba beneen yoon, xalaatal ci ndànk-ndànk ci Wolof, te defal sa tontu mu mujj mi ci \\boxed{}."
        ),
        "labels": {
            "problem_target": "Jafe-jafe",
            "problem_english": "Tekki bu àngale bu jafe-jafe bi",
            "solution_english": "Saafara bu jub bu ñu jox ci àngale",
            "ref_begin": "=== Njàlbéen Saafara bu Ñu Jox ===",
            "ref_end": "=== Mujj Saafara bu Ñu Jox ===",
        },
    },

    "YOR": {
        "student_instruction": (
            "Jọ̀wọ́ ronú ní ìgbésẹ̀-ní-ìgbésẹ̀, kí o sì fi ìdáhùn ìkẹyìn rẹ sínú \\boxed{}."
        ),
        "think_prefix": (
            "Gẹ́gẹ́ bí a ti béèrè, màá bẹ̀rẹ̀ sí í ronú ní èdè Yorùbá."
        ),
        "reason_first_prompt": (
            "Ojútùú àpẹẹrẹ Gẹ̀ẹ́sì tó wà lókè yìí dé sí ìdáhùn tó tọ́. "
            "Jọ̀wọ́ ṣe àyẹ̀wò ojútùú yìí, kí o sì ṣàlàyé àwọn ìgbésẹ̀ ìrònú pàtàkì àti àwọn ọgbọ́n tí a lò láti yanju ìṣòro náà. "
            "Má ṣe lo àmì <think>. Má ṣe dá ojútùú tirẹ̀ jáde síbẹ̀. "
            "Ṣe àyẹ̀wò àti àlàyé ojútùú àpẹẹrẹ tí a fún ọ nìkan."
        ),
        "transition_prompt": (
            "Lẹ́yìn tí o bá ti ka ojútùú àpẹẹrẹ Gẹ̀ẹ́sì tó wà lókè yìí, rí i dájú pé o lóye ìrònú tó wà lẹ́yìn ìgbésẹ̀ kọ̀ọ̀kan gan-an—"
            "má ṣe daakọ rẹ̀ tàbí tún un sọ ní ọ̀rọ̀ míràn lasan. "
            "Ní báyìí, lo ọ̀rọ̀ tirẹ̀ àti ìrònú olómìnira rẹ láti yanju ìṣòro ìbẹ̀rẹ̀ náà ní èdè Yorùbá. "
            "Ronú ní ìgbésẹ̀-ní-ìgbésẹ̀, gbìmọ̀ ọ̀nà oríṣiríṣi, má sì bẹ̀rù láti padà sẹ́yìn tàbí tún ronú bí ohun kan kò bá ṣiṣẹ́:"
        ),
        "teacher_final_instruction": (
            "Jọ̀wọ́ ronú ní ìgbésẹ̀-ní-ìgbésẹ̀ ní èdè Yorùbá, kí o sì fi ìdáhùn ìkẹyìn rẹ sínú \\boxed{}."
        ),
        "labels": {
            "problem_target": "Ìṣòro",
            "problem_english": "Ìtumọ̀ Gẹ̀ẹ́sì ti ìṣòro náà",
            "solution_english": "Ojútùú àpẹẹrẹ Gẹ̀ẹ́sì tó tọ́",
            "ref_begin": "=== Ìbẹ̀rẹ̀ Ojútùú Àpẹẹrẹ ===",
            "ref_end": "=== Òpin Ojútùú Àpẹẹrẹ ===",
        },
    },

    # ============================================================
    # East Africa
    # ============================================================
    "AMH": {
        "student_instruction": (
            "እባክዎ ደረጃ በደረጃ ያስቡ፣ የመጨረሻ መልስዎንም በ \\boxed{} ውስጥ ያስቀምጡ።"
        ),
        "think_prefix": (
            "በጥያቄው መሠረት፣ በአማርኛ ማሰብ እጀምራለሁ።"
        ),
        "reason_first_prompt": (
            "ከላይ ያለው የእንግሊዝኛ ማጣቀሻ መፍትሄ ወደ ትክክለኛው መልስ ይደርሳል። "
            "እባክዎ ይህን መፍትሄ ይተንትኑ፣ ዋና ዋና የምክንያት ደረጃዎችንና የችግር መፍቻ ስልቶችን ያብራሩ። "
            "<think> መለያዎችን አይጠቀሙ። ገና የራስዎን መፍትሄ አያውጡ። "
            "የተሰጠውን ማጣቀሻ መፍትሄ ብቻ ይተንትኑና ያብራሩ።"
        ),
        "transition_prompt": (
            "ከላይ ያለውን የእንግሊዝኛ ማጣቀሻ መፍትሄ ካነበቡ በኋላ፣ ከእያንዳንዱ ደረጃ በስተጀርባ ያለውን ምክንያት በእውነት መረዳትዎን ያረጋግጡ—"
            "አይቅዱት ወይም በሌላ ቃላት ብቻ አይድገሙት። "
            "አሁን በራስዎ ቃላትና በገለልተኛ ምክንያታዊ አስተሳሰብ፣ ዋናውን ችግር በአማርኛ ይፍቱ። "
            "ደረጃ በደረጃ ያስቡ፣ የተለያዩ መንገዶችን ይሞክሩ፣ ነገር ካልሰራ ደግሞ ወደ ኋላ መመለስን ወይም እንደገና ማሰብን አይፍሩ፦"
        ),
        "teacher_final_instruction": (
            "እባክዎ በአማርኛ ደረጃ በደረጃ ያስቡ፣ የመጨረሻ መልስዎንም በ \\boxed{} ውስጥ ያስቀምጡ።"
        ),
        "labels": {
            "problem_target": "ችግር",
            "problem_english": "የችግሩ የእንግሊዝኛ ትርጉም",
            "solution_english": "ትክክለኛው የእንግሊዝኛ ማጣቀሻ መፍትሄ",
            "ref_begin": "=== የማጣቀሻ መፍትሄ መጀመሪያ ===",
            "ref_end": "=== የማጣቀሻ መፍትሄ መጨረሻ ===",
        },
    },

    "KIN": {
        "student_instruction": (
            "Nyamuneka tekereza intambwe ku yindi, kandi ushyire igisubizo cya nyuma muri \\boxed{}."
        ),
        "think_prefix": (
            "Nk'uko byasabwe, ngiye gutangira gutekereza mu Kinyarwanda."
        ),
        "reason_first_prompt": (
            "Igisubizo ntangarugero cyo mu Cyongereza kiri haruguru kigera ku gisubizo nyacyo. "
            "Nyamuneka sesengura iki gisubizo, usobanure intambwe z'ingenzi z'imitekerereze n'ingamba zakoreshejwe mu gukemura ikibazo. "
            "Ntukoreshe ibimenyetso bya <think>. Ntukore igisubizo cyawe bwite ubu. "
            "Sesengura kandi usobanure gusa igisubizo ntangarugero cyatanzwe."
        ),
        "transition_prompt": (
            "Nyuma yo gusoma igisubizo ntangarugero cyo mu Cyongereza kiri haruguru, banza wemeze ko usobanukiwe by'ukuri impamvu iri inyuma ya buri ntambwe—"
            "ntukigane kandi ntugisubiremo mu yandi magambo gusa. "
            "Ubu rero, ukoresheje amagambo yawe bwite n'ibitekerezo byawe byigenga, komeza ukemure ikibazo cy'umwimerere mu Kinyarwanda. "
            "Tekereza intambwe ku yindi, gerageza uburyo butandukanye, kandi ntutinye gusubira inyuma cyangwa kongera gutekereza niba hari ikidakoze:"
        ),
        "teacher_final_instruction": (
            "Nyamuneka tekereza intambwe ku yindi mu Kinyarwanda, kandi ushyire igisubizo cya nyuma muri \\boxed{}."
        ),
        "labels": {
            "problem_target": "Ikibazo",
            "problem_english": "Ubusobanuro bw'ikibazo mu Cyongereza",
            "solution_english": "Igisubizo ntangarugero nyacyo cyo mu Cyongereza",
            "ref_begin": "=== Intangiriro y'Igisubizo Ntangarugero ===",
            "ref_end": "=== Iherezo ry'Igisubizo Ntangarugero ===",
        },
    },

    "LUG": {
        "student_instruction": (
            "Nsaba lowooza mutendera ku mutendera, era oteeke eky'okuddamu ekisembayo mu \\boxed{}."
        ),
        "think_prefix": (
            "Nga bwe kisabiddwa, nja kutandika okulowooza mu Luganda."
        ),
        "reason_first_prompt": (
            "Ennyinyonnyola ey'ekyokulabirako mu Lungereza waggulu etuuka ku ky'okuddamu ekituufu. "
            "Nsaba weekenneenye ennyinyonnyola eno, onnyonnyole emitendera emikulu egy'okulowooza n'obukodyo obwakozesebwa okugonjoola ekibuuzo. "
            "Tokozesa bubonero bwa <think>. Tonnavaayo na ngeri yo ey'okugonjoola. "
            "Weekenneenye era onnyonnyole ennyinyonnyola ey'ekyokulabirako eweereddwa yokka."
        ),
        "transition_prompt": (
            "Oluvannyuma lw'okusoma ennyinyonnyola ey'ekyokulabirako mu Lungereza waggulu, kakasa nti otegedde ddala ensonga eri emabega wa buli mutendera—"
            "togikoppa era togiddamu mu bigambo birala byokka. "
            "Kati, kozesa ebigambo byo n'okulowooza kwo okwetengeredde okugonjoola ekibuuzo ekyasooka mu Luganda. "
            "Lowooza mutendera ku mutendera, gezaako amakubo ag'enjawulo, era totya kudda mabega oba okuddamu okulowooza singa ekintu tekikola:"
        ),
        "teacher_final_instruction": (
            "Nsaba lowooza mutendera ku mutendera mu Luganda, era oteeke eky'okuddamu ekisembayo mu \\boxed{}."
        ),
        "labels": {
            "problem_target": "Ekibuuzo",
            "problem_english": "Okuvvuunula kw'ekibuuzo mu Lungereza",
            "solution_english": "Ennyinyonnyola ey'ekyokulabirako entuufu mu Lungereza",
            "ref_begin": "=== Entandikwa y'Ennyinyonnyola ey'Ekyokulabirako ===",
            "ref_end": "=== Enkomerero y'Ennyinyonnyola ey'Ekyokulabirako ===",
        },
    },

    "SWA": {
        "student_instruction": (
            "Tafadhali fikiri hatua kwa hatua, na uweke jibu lako la mwisho ndani ya \\boxed{}."
        ),
        "think_prefix": (
            "Kwa ombi, nitaanza kufikiria kwa Kiswahili."
        ),
        "reason_first_prompt": (
            "Suluhisho la rejeleo la Kiingereza hapo juu linafikia jibu sahihi. "
            "Tafadhali chambua suluhisho hili na ueleze hatua kuu za hoja pamoja na mikakati ya utatuzi iliyotumika. "
            "USITUMIE alama za <think>. Usitoe suluhisho lako mwenyewe bado. "
            "Chambua na eleza tu suluhisho la rejeleo ulilopewa."
        ),
        "transition_prompt": (
            "Baada ya kusoma suluhisho la rejeleo la Kiingereza hapo juu, hakikisha umeelewa kweli mantiki ya kila hatua—"
            "usilinakili wala kulifafanua upya tu. "
            "Sasa, kwa kutumia maneno yako mwenyewe na hoja huru, tatua swali la asili kwa Kiswahili. "
            "Fikiri hatua kwa hatua, jaribu mbinu tofauti, na usiogope kurudi nyuma au kufikiria upya ikiwa jambo fulani halifanyi kazi:"
        ),
        "teacher_final_instruction": (
            "Tafadhali fikiri hatua kwa hatua kwa Kiswahili, na uweke jibu lako la mwisho ndani ya \\boxed{}."
        ),
        "labels": {
            "problem_target": "Swali",
            "problem_english": "Tafsiri ya Kiingereza ya swali",
            "solution_english": "Suluhisho sahihi la rejeleo kwa Kiingereza",
            "ref_begin": "=== Mwanzo wa Suluhisho la Rejeleo ===",
            "ref_end": "=== Mwisho wa Suluhisho la Rejeleo ===",
        },
    },

    "ORM": {
        "student_instruction": (
            "Maaloo tartiiba tartiibaan yaadi, deebii kee isa dhumaa \\boxed{} keessa kaa'i."
        ),
        "think_prefix": (
            "Gaaffii kanaan, Afaan Oromootiin yaaduu nan jalqaba."
        ),
        "reason_first_prompt": (
            "Furmaanni wabii Afaan Ingiliffaan armaan olii deebii sirrii irra ga'a. "
            "Maaloo furmaata kana xiinxali, tarkaanfiiwwan yaada ijoo fi tooftaalee rakkoo furuuf itti fayyadamaman ibsi. "
            "Mallattoolee <think> hin fayyadamin. Amma furmaata kee mataa keetii hin baasini. "
            "Furmaata wabii kenname qofa xiinxalii ibsi."
        ),
        "transition_prompt": (
            "Furmaata wabii Afaan Ingiliffaan armaan olii erga dubbistee booda, sababa tarkaanfii tokkoon tokkoon duuba jiru dhuguma hubachuu kee mirkaneessi—"
            "hin garagalchin yookaan jechoota biraatiin qofa hin ibsin. "
            "Amma jechoota kee fi yaada of danda'een rakkoo jalqabaa Afaan Oromootiin furi. "
            "Tartiiba tartiibaan yaadi, mala gara garaa yaali, wanti tokko yoo hin hojjenne immoo duubatti deebi'uu yookaan irra deebi'anii yaaduu hin sodaatin:"
        ),
        "teacher_final_instruction": (
            "Maaloo Afaan Oromootiin tartiiba tartiibaan yaadi, deebii kee isa dhumaa \\boxed{} keessa kaa'i."
        ),
        "labels": {
            "problem_target": "Rakkoo",
            "problem_english": "Hiika Ingiliffaa rakkoo kanaa",
            "solution_english": "Furmaata wabii sirrii Afaan Ingiliffaa",
            "ref_begin": "=== Jalqaba Furmaata Wabii ===",
            "ref_end": "=== Xumura Furmaata Wabii ===",
        },
    },

    # ============================================================
    # Southern Africa
    # ============================================================
    "SNA": {
        "student_instruction": (
            "Ndapota funga nhanho nenhanho, uye isa mhinduro yako yekupedzisira mukati me \\boxed{}."
        ),
        "think_prefix": (
            "Sekukumbirwa, ndichatanga kufunga nechiShona."
        ),
        "reason_first_prompt": (
            "Mhinduro yereferensi yeChirungu iri pamusoro inosvika pamhinduro yakarurama. "
            "Ndapota ongorora mhinduro iyi uye tsanangura nhanho huru dzekufunga pamwe nemazano akashandiswa kugadzirisa dambudziko. "
            "Usashandise ma tag e <think>. Usati waburitsa mhinduro yako wega. "
            "Ongorora uye tsanangura chete mhinduro yereferensi yawapiwa."
        ),
        "transition_prompt": (
            "Mushure mekuverenga mhinduro yereferensi yeChirungu iri pamusoro, iva nechokwadi chokuti wanyatsonzwisisa kufunga kuri kuseri kwenhanho imwe neimwe—"
            "usai kopi kana kungoitsanangura nemamwe mashoko. "
            "Zvino, uchishandisa mashoko ako uye kufunga kwakazvimirira, gadzirisa dambudziko rekutanga nechiShona. "
            "Funga nhanho nenhanho, edza nzira dzakasiyana, uye usatya kudzokera shure kana kufungazve kana chimwe chinhu chikasashanda:"
        ),
        "teacher_final_instruction": (
            "Ndapota funga nhanho nenhanho nechiShona, uye isa mhinduro yako yekupedzisira mukati me \\boxed{}."
        ),
        "labels": {
            "problem_target": "Dambudziko",
            "problem_english": "Dudziro yeChirungu yedambudziko",
            "solution_english": "Mhinduro yereferensi yeChirungu yakarurama",
            "ref_begin": "=== Kutanga kweMhinduro yeReferensi ===",
            "ref_end": "=== Kupera kweMhinduro yeReferensi ===",
        },
    },

    "XHO": {
        "student_instruction": (
            "Nceda ucinge inyathelo ngenyathelo, uze ufake impendulo yakho yokugqibela ngaphakathi kwe \\boxed{}."
        ),
        "think_prefix": (
            "Ngokwesicelo, ndiza kuqalisa ukucinga ngesiXhosa."
        ),
        "reason_first_prompt": (
            "Isisombululo sesalathiso sesiNgesi esingasentla sifikelela kwimpendulo echanekileyo. "
            "Nceda uhlalutye esi sisombululo, uchaze amanyathelo aphambili okucinga kunye namaqhinga okusombulula ingxaki asetyenzisiweyo. "
            "Musa ukusebenzisa iithegi ze <think>. Musa ukuvelisa esakho isisombululo okwangoku. "
            "Hlalutya uze uchaze kuphela isisombululo sesalathiso osinikiweyo."
        ),
        "transition_prompt": (
            "Emva kokufunda isisombululo sesalathiso sesiNgesi esingasentla, qinisekisa ukuba uyayiqonda ngokwenene ingqiqo esemva kwenyathelo ngalinye—"
            "musa ukusikhuphela okanye ukusiphinda ngamanye amagama kuphela. "
            "Ngoku, sebenzisa amazwi akho kunye nengqiqo ezimeleyo ukusombulula ingxaki yokuqala ngesiXhosa. "
            "Cinga inyathelo ngenyathelo, zama iindlela ezahlukeneyo, kwaye ungoyiki ukubuyela emva okanye uphinde ucinge ukuba into ethile ayisebenzi:"
        ),
        "teacher_final_instruction": (
            "Nceda ucinge inyathelo ngenyathelo ngesiXhosa, uze ufake impendulo yakho yokugqibela ngaphakathi kwe \\boxed{}."
        ),
        "labels": {
            "problem_target": "Ingxaki",
            "problem_english": "Uguqulelo lwesiNgesi lwengxaki",
            "solution_english": "Isisombululo sesalathiso sesiNgesi esichanekileyo",
            "ref_begin": "=== Ukuqala kweSisombululo seSalathiso ===",
            "ref_end": "=== Ukuphela kweSisombululo seSalathiso ===",
        },
    },

    "ZUL": {
        "student_instruction": (
            "Sicela ucabange isinyathelo ngesinyathelo, bese ufaka impendulo yakho yokugcina ngaphakathi kwe \\boxed{}."
        ),
        "think_prefix": (
            "Ngokwesicelo, ngizoqala ukucabanga ngesiZulu."
        ),
        "reason_first_prompt": (
            "Isixazululo esiyireferensi sesiNgisi esingenhla sifinyelela empendulweni efanele. "
            "Sicela usihlaziye lesi sixazululo futhi uchaze izinyathelo ezisemqoka zokucabanga namasu asetshenzisiwe ekuxazululeni inkinga. "
            "Ungasebenzisi amathegi athi <think>. Ungakhiphi isixazululo sakho okwamanje. "
            "Hlaziya futhi uchaze kuphela isixazululo esiyireferensi osinikiwe."
        ),
        "transition_prompt": (
            "Ngemva kokufunda isixazululo esiyireferensi sesiNgisi esingenhla, qinisekisa ukuthi uyiqonda ngempela imbangela nengqondo esemva kwesinyathelo ngasinye—"
            "ungasikopishi noma usiphinde ngamanye amagama kuphela. "
            "Manje, usebenzisa amazwi akho nokucabanga kwakho okuzimele, xazulula inkinga yokuqala ngesiZulu. "
            "Cabanga isinyathelo ngesinyathelo, zama izindlela ezahlukene, futhi ungesabi ukubuyela emuva noma ukucabanga kabusha uma okuthile kungasebenzi:"
        ),
        "teacher_final_instruction": (
            "Sicela ucabange isinyathelo ngesinyathelo ngesiZulu, bese ufaka impendulo yakho yokugcina ngaphakathi kwe \\boxed{}."
        ),
        "labels": {
            "problem_target": "Inkinga",
            "problem_english": "Ukuhumusha kwesiNgisi kwenkinga",
            "solution_english": "Isixazululo esiyireferensi sesiNgisi esifanele",
            "ref_begin": "=== Ukuqala kweSixazululo seReferensi ===",
            "ref_end": "=== Ukuphela kweSixazululo seReferensi ===",
        },
    },

    "SOT": {
        "student_instruction": (
            "Ka kopo nahana mohato ka mohato, 'me u kenye karabo ea hao ea ho qetela ka hare ho \\boxed{}."
        ),
        "think_prefix": (
            "Ho latela kopo, ke tla qala ho nahana ka Sesotho."
        ),
        "reason_first_prompt": (
            "Tharollo ea mohlala ea Senyesemane e ka holimo e fihla karabong e nepahetseng. "
            "Ka kopo sekaseka tharollo ena, 'me u hlalose mehato ea bohlokoa ea monahano le maano a sebelisitsoeng ho rarolla bothata. "
            "Se ke oa sebelisa matšoao a <think>. U se ke oa hlahisa tharollo ea hao hona joale. "
            "Sekaseka feela 'me u hlalose tharollo ea mohlala e fanoeng."
        ),
        "transition_prompt": (
            "Ka mor'a ho bala tharollo ea mohlala ea Senyesemane e ka holimo, etsa bonnete ba hore u utloisisa kannete lebaka le ka mora mohato ka mong—"
            "u se ke oa e kopitsa kapa oa e pheta ka mantsoe a mang feela. "
            "Joale, sebelisa mantsoe a hao le monahano oa hao o ikemetseng ho rarolla bothata ba pele ka Sesotho. "
            "Nahana mohato ka mohato, leka mekhoa e fapaneng, 'me u se ke oa tšaba ho khutlela morao kapa ho nahana hape haeba ntho e sa sebetse:"
        ),
        "teacher_final_instruction": (
            "Ka kopo nahana mohato ka mohato ka Sesotho, 'me u kenye karabo ea hao ea ho qetela ka hare ho \\boxed{}."
        ),
        "labels": {
            "problem_target": "Bothata",
            "problem_english": "Phetolelo ea Senyesemane ea bothata",
            "solution_english": "Tharollo ea mohlala e nepahetseng ea Senyesemane",
            "ref_begin": "=== Qalo ea Tharollo ea Mohlala ===",
            "ref_end": "=== Qetello ea Tharollo ea Mohlala ===",
        },
    },

    # ============================================================
    # Central Africa
    # ============================================================
    "LIN": {
        "student_instruction": (
            "Nabondeli yo, kanisá litambe na litambe, mpe tyá eyano na yo ya nsuka na kati ya \\boxed{}."
        ),
        "think_prefix": (
            "Na kolanda bosengi, nakobanda kokanisa na Lingála."
        ),
        "reason_first_prompt": (
            "Solution ya référence na Anglais oyo ezali likoló ekómi na eyano ya solo. "
            "Nabondeli yo, talelá solution yango malamu, mpe limbolá litambe ya ntina ya makanisi mpe mayele oyo esalelamaki mpo na kosilisa mokakatano. "
            "Kosalela bilembo ya <think> te. Kobimisa naino solution na yo moko te. "
            "Talelá mpe limbolá kaka solution ya référence oyo epesami."
        ),
        "transition_prompt": (
            "Nsima ya kotánga solution ya référence na Anglais oyo ezali likoló, yebá malamu ete ososoli solo makanisi oyo ezali nsima ya litambe mokomoko—"
            "kokopela yango te mpe kozongela yango kaka na maloba mosusu te. "
            "Sikoyo, salelá maloba na yo moko mpe makanisi na yo moko mpo na kosilisa mokakatano ya ebandeli na Lingála. "
            "Kanisá litambe na litambe, meká banzela ndenge na ndenge, mpe kobanga te kozonga sima to kokanisa lisusu soki likambo moko esali te:"
        ),
        "teacher_final_instruction": (
            "Nabondeli yo, kanisá litambe na litambe na Lingála, mpe tyá eyano na yo ya nsuka na kati ya \\boxed{}."
        ),
        "labels": {
            "problem_target": "Mokakatano",
            "problem_english": "Libongoli ya mokakatano na Anglais",
            "solution_english": "Solution ya référence ya solo na Anglais",
            "ref_begin": "=== Ebandeli ya Solution ya Référence ===",
            "ref_end": "=== Nsuka ya Solution ya Référence ===",
        },
    },
}

for code, cfg in AFRICAN_LANGUAGE_CONFIG.items():
    cfg["teacher_final_instruction"] = cfg["student_instruction"]

# Optional compatibility:
LANGUAGE_CONFIG.update(AFRICAN_LANGUAGE_CONFIG)
LANGUAGE_CONFIG["SW"] = LANGUAGE_CONFIG["SWA"]