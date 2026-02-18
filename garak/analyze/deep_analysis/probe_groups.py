# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Information about probe groups and categorization
"""

PROBE_GROUP_DESCRIPTIONS = {
    "jailbreak": "A set of probes that assess the efficacy of jailbreaks. "
    "Jailbreaks are prompts that aim to bypass a model's alignment.",
    "system": "A set of probes that assess the potential systemic impacts of model inputs. "
    "The results of these probes are generally most applicable to agentic systems, "
    "including retrieval augmented generation (RAG) and can suggest meaningful security impacts.",
    "tokenizer": "A set of probes that consider impacts that relate to tokenizers and may allow for unexpected "
    "behavior, potentially including system and jailbreak.",
    "code": "A set of probes that explore the potential for code-related risks including package hallucination. "
    "These probes provide insight into risks that may lead to the execution of malicious code.",
    "misleading": "A set of probes that consider the potential for models to produce misinformation.",
    "training_data": "A set of probes that seek to elicit the reproduction of possibly copyrighted data from a target.",
    "harm": "A set of probes that seek to elicit inappropriate or otherwise harmful language from a target.",
    "bypass": "A set of probes associated with techniques commonly used to bypass filter-based detections. "
    "High scores in this category suggest that the target is susceptible to the use of encoded prompts that "
    "may not be detected by all input filters or application firewalls.",
}

TIER_1_PROBE_GROUPS = {
    "jailbreak": [
        "dan.DanInTheWild",
        "dan.DanInTheWildMini",
        "grandma.Slurs",
        "grandma.Substances",
        "latentinjection.LatentInjectionFactSnippetEiffel",
        "latentinjection.LatentInjectionReport",
        "latentinjection.LatentInjectionResume",
        "latentinjection.LatentInjectionTranslationEnFr",
        "latentinjection.LatentInjectionTranslationEnZh",
        "latentinjection.LatentJailbreak",
        "latentinjection.LatentJailbreakMini",
    ],
    "system": [
        "ansiescape.AnsiRaw",
        "latentinjection.LatentInjectionFactSnippetEiffel",
        "latentinjection.LatentInjectionReport",
        "latentinjection.LatentInjectionResume",
        "latentinjection.LatentInjectionTranslationEnFr",
        "latentinjection.LatentInjectionTranslationEnZh",
        "latentinjection.LatentJailbreak",
        "latentinjection.LatentJailbreakMini",
        "xss.MarkdownImageExfil",
        "fileformats.HF_Files",
    ],
    "tokenizer": ["goodside.Tag"],
    "code": [
        "packagehallucination.JavaScript",
        "packagehallucination.Python",
        "packagehallucination.Ruby",
        "packagehallucination.Rust",
    ],
    "misleading": [],
    "training_data": [
        "leakreplay.GuardianComplete",
        "leakreplay.LiteratureComplete",
        "leakreplay.LiteratureComplete80",
        "leakreplay.NYTComplete",
        "leakreplay.PotterComplete",
    ],
    "harm": ["grandma.Slurs", "grandma.Substances", "realtoxicityprompts.RTPBlank"],
    "bypass": [
        "encoding.InjectBase64",
        "encoding.InjectQP",
        "encoding.InjectUU",
        "goodside.Tag",
    ],
}

TIER_2_PROBE_GROUPS = {
    "jailbreak": [
        "dan.Ablation_Dan_11_0",
        "dan.AutoDAN",
        "dan.AutoDANCached",
        "goodside.ThreatenJSON",
        "promptinject.HijackHateHumans",
        "promptinject.HijackHateHumansMini",
        "promptinject.HijackKillHumans",
        "promptinject.HijackKillHumansMini",
        "promptinject.HijackLongPrompt",
        "promptinject.HijackLongPromptMini",
        "suffix.BEAST",
        "suffix.GCG",
        "suffix.GCGCached",
        "tap.PAIR",
        "tap.TAP",
        "tap.TAPCached",
        "visual_jailbreak.FigStep",
        "visual_jailbreak.FigStepTiny",
    ],
    "system": [],
    "tokenizer": [],
    "code": [
        "malwaregen.Evasion",
        "malwaregen.Payload",
        "malwaregen.SubFunctions",
        "malwaregen.TopLevel",
    ],
    "misleading": [
        "goodside.WhoIsRiley",
        "misleading.FalseAssertion50",
        "snowball.GraphConnectivity",
        "snowball.GraphConnectivityMini",
    ],
    "training_data": [
        "grandma.Win10",
        "grandma.Win11",
        "leakreplay.GuardianCloze",
        "leakreplay.LiteratureCloze",
        "leakreplay.LiteratureCloze80",
        "leakreplay.NYTCloze",
        "leakreplay.PotterCloze",
        "divergence.Repeat",
        "divergence.RepeatExtended",
    ],
    "harm": [
        "atkgen.Tox",
        "continuation.ContinueSlursReclaimedSlurs",
        "continuation.ContinueSlursReclaimedSlursMini",
        "lmrc.Bullying",
        "lmrc.Deadnaming",
        "lmrc.QuackMedicine",
        "lmrc.SexualContent",
        "lmrc.Sexualisation",
        "lmrc.SlurUsage",
        "topic.WordnetControversial",
    ],
    "bypass": [
        "encoding.InjectAscii85",
        "encoding.InjectBase16",
        "encoding.InjectBase2048",
        "encoding.InjectBase32",
        "encoding.InjectBraille",
        "encoding.InjectEcoji",
        "encoding.InjectHex",
        "encoding.InjectMime",
        "encoding.InjectMorse",
        "encoding.InjectNato",
        "encoding.InjectROT13",
        "encoding.InjectZalgo",
    ],
}
