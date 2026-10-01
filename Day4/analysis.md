# Day 4 Assessment — Will It Fit, and May I Use It?

## Scenario

I want to run an open LLM locally on my 8 GB RAM laptop without a dedicated GPU. The purpose is to use the model as a personal coding assistant for Java, Python and Data Structures and Algorithms questions.

The model will be used by me for academic and learning purposes. My available memory budget is 8 GB. I will begin with an 8K-token context and examine how increasing the context affects memory usage.

Before selecting a model, I will consider both its memory requirements and its licence conditions. The licence must permit my intended use, and I will verify the exact licence from the official model card.

## 1. Explanation of Key Concepts

### 1.1 Model Weights

Model weights are the stored numerical parameters of an LLM. Their memory requirement mainly depends on the number of parameters and the number of bytes used for each parameter.

In my scenario, I have an 8 GB memory budget. For example, an 8B model using Q4_K_M requires fewer bytes per parameter than the same 8B model using FP16. Therefore, the weights occupy much less memory with Q4_K_M.

If I ignore the weight size, I may choose a model that cannot fit in my available memory. The limitation is that this calculation estimates the memory required for the weights and does not represent the complete runtime memory usage by itself.

### 1.2 Quantization

Quantization reduces the number of bytes used to represent model parameters. Lower-precision formats such as Q4_K_M use less memory than FP16.

I used different quantization levels for the same 8B model while keeping the context length at 8K. This allows me to observe how changing precision affects the weights and total memory.

If I ignore quantization, I may unnecessarily choose a model that requires too much memory. However, using lower precision can involve a quality trade-off, so reducing memory is not the only consideration.

### 1.3 KV Cache and Context Length

The KV cache stores information needed by the model while processing the context. Its memory requirement grows as the context length increases.

In my scenario, I tested an 8B Q4_K_M model at 4K, 8K, 32K and 128K context lengths. The model weights remain the same, but the KV cache increases as the context grows.

If I ignore context length, a model that fits at a short context may stop fitting when a longer conversation or larger amount of information is kept in the context. This is especially relevant for an AI coding assistant or agent that may accumulate tool results.

The formula is an estimate, so actual memory usage can differ because of the model architecture, runtime settings and implementation.

### 1.4 Model Card

A model card is the documentation provided for a model. It contains information such as the model name, publisher, parameters, context information, licence and capabilities.

For my scenario, I use the official model card when comparing candidate models. I check the model's licence and whether tool calling is stated before deciding whether it is suitable.

If I ignore the model card, I may incorrectly assume that a model can be used or redistributed in a particular way.

### 1.5 Open-Weight vs Open-Source Licensing

An open-weight model provides access to model weights, but open-weight does not automatically mean that the model is open-source under the same conditions as conventional open-source software.

The exact licence and its conditions determine what uses and redistribution are permitted. Therefore, I check the exact licence name and conditions rather than deciding only from the fact that the model weights are available.

For my scenario, the licence is part of the selection decision along with memory requirements. A model that fits my laptop is not automatically suitable if its licence does not permit my intended use.

## 2. Memory Estimate Table

The available memory in my scenario is 8 GB. I used the Day 4 memory formula:

- Weights = parameters × bytes per parameter
- KV cache = parameters × context in K tokens × 0.02
- Total = (weights + KV cache) × 1.10

| Model | Params (B) | Precision | Context (K) | Weights (GB) | KV cache (GB) | Total (GB) | Fits in 8 GB? |
|---|---:|---|---:|---:|---:|---:|---|
| 1.5B Q4_K_M | 1.5 | Q4_K_M | 8 | 0.86 | 0.24 | 1.20 | Yes |
| 8B Q4_K_M | 8.0 | Q4_K_M | 8 | 4.56 | 1.28 | 6.42 | Yes, but tight |
| 8B FP16 | 8.0 | FP16 | 8 | 16.00 | 1.28 | 19.01 | No |
| 30B Q4_K_M | 30.0 | Q4_K_M | 8 | 17.10 | 4.80 | 24.09 | No |

### Observation

The 1.5B Q4_K_M configuration fits comfortably within my 8 GB memory budget. The 8B Q4_K_M configuration also fits according to the estimate, but it is close to the available limit. The 8B FP16 and 30B Q4_K_M configurations exceed the 8 GB budget.

The estimate is useful for deciding whether a model is likely to fit before downloading it. It should not be treated as an exact prediction of runtime memory usage because actual usage can differ depending on the model architecture, runtime and configuration.

## 3. Context Length and Quantization Observation

I used the 8B Q4_K_M configuration for these experiments and kept the available memory at 8 GB.

### 3.1 Context Length Experiment

The quantization was kept fixed at Q4_K_M while the context length was changed.

| Setting changed | Value used | Weights (GB) | KV cache (GB) | Total (GB) | Fits? |
|---|---:|---:|---:|---:|---|
| Context length | 4K | 4.56 | 0.64 | 5.72 | Yes |
| Context length | 8K | 4.56 | 1.28 | 6.42 | Yes, but tight |
| Context length | 32K | 4.56 | 5.12 | 10.65 | No |
| Context length | 128K | 4.56 | 20.48 | 27.54 | No |

As the context length increased, the model weights remained unchanged at 4.56 GB. The KV cache increased because it depends on the context length. Therefore, the total memory requirement increased.

For my 8 GB machine, the largest tested context that fits at Q4_K_M is 8K. At 32K, the estimated total exceeds the available memory.

### 3.2 Quantization Experiment

The context length was kept fixed at 8K while the quantization was changed.

| Setting changed | Value used | Weights (GB) | KV cache (GB) | Total (GB) | Fits? |
|---|---:|---:|---:|---:|---|
| Quantization | Q3_K_M | 3.44 | 1.28 | 5.19 | Yes |
| Quantization | Q4_K_M | 4.56 | 1.28 | 6.42 | Yes, but tight |
| Quantization | Q5_K_M | 5.44 | 1.28 | 7.39 | Yes, but tight |
| Quantization | Q8_0 | 8.00 | 1.28 | 10.21 | No |
| Quantization | FP16 | 16.00 | 1.28 | 19.01 | No |

When quantization changed, the weight memory changed while the KV cache remained the same because the context length and model parameter count were unchanged.

For my scenario, I would choose Q4_K_M as a balance between memory usage and model quality. Q3_K_M uses less memory but may involve a greater quality trade-off, while Q5_K_M is closer to the 8 GB limit.

## 4. Open Model Comparison

I compared three open models from different model families. The information below is based on the official model card and the corresponding Ollama library page.

Model 1: Qwen
Full model name and version: Qwen3:8B
Publisher: Qwen
Total / active parameters (MoE?): 8.19B / 8.19B (dense)
Context window: 40K tokens
Licence (exact name): Apache License Version 2.0
Commercial use allowed?: Yes, subject to Apache 2.0 terms
Any extra conditions?: Apache 2.0 licence conditions
Tool calling stated on the card?: Yes
GGUF / Ollama build available?: Yes
Download size at Q4: 5.2 GB
Your memory estimate (total): 6.42 GB at 8K Q4_K_M
Fits your scenario's machine?: Yes, but tight
Date you checked the card: 2026-10-01

Model 2: Mistral
Full model name and version: Mistral-7B-v0.3
Publisher: Mistral AI
Total / active parameters (MoE?): 7B / 7B (dense)
Context window: 32K tokens
Licence (exact name): Apache-2.0
Commercial use allowed?: Yes, subject to Apache-2.0 terms
Any extra conditions?: Apache-2.0 licence conditions
Tool calling stated on the card?: Yes — function calling is supported for v0.3
GGUF / Ollama build available?: Yes
Download size at Q4: 4.4 GB
Your memory estimate (total): 5.64 GB at 7B, Q4_K_M, 8K
Fits your scenario's machine?: Yes
Date you checked the card: 2026-10-01

Model 3: IBM Granite 4.1
Full model name and version: Granite-4.1-8B
Publisher: IBM
Total / active parameters (MoE?): 8B / 8B (dense)
Context window: 128K tokens
Licence (exact name): Apache 2.0
Commercial use allowed?: Yes, subject to Apache 2.0 terms
Any extra conditions?: Apache 2.0 licence conditions
Tool calling stated on the card?: Yes
GGUF / Ollama build available?: Yes
Download size at Q4: 5.3 GB
Your memory estimate (total): 6.42 GB at 8K Q4_K_M
Fits your scenario's machine?: Yes, but tight
Date you checked the card: 2026-10-01

## 5. Estimate Versus Reality

I ran the selected model using Ollama and compared the actual reported model size and running memory with the values predicted by my estimator.

| Model | ollama list size | ollama ps size | Processor (CPU / GPU / split) | Your estimate (weights / total) |
|---|---:|---:|---|---:|
| Qwen3:8b | [actual value] | [actual value] | [actual value] | 4.56 GB / 6.42 GB |

The estimated memory was compared with the actual runtime information reported by Ollama. Any difference can be explained by factors such as the model's actual quantization, runtime overhead, context setting and model architecture.

The processor information shows whether the model is being processed by the CPU, GPU, or a combination of both.

## 6. Suitability Analysis

For my scenario, I recommend **Mistral-7B-v0.3** using a Q4_K_M quantization with an 8K context.

The model has approximately 7B parameters and uses the Apache-2.0 licence. At 8K context with Q4_K_M, my estimator gives approximately 5.64 GB of total memory, which is within my 8 GB memory budget. This gives more memory headroom than the 8B Q4_K_M configuration while still providing a model suitable for a coding-assistant scenario.

The licence is also important because Apache-2.0 provides clear terms for use and redistribution, subject to its licence conditions. The model documentation also states function-calling support, which can be useful if the coding assistant is later extended into an agent that uses tools.

### Runner-up

My runner-up is **Qwen3:8B** with Q4_K_M and an 8K context. Its estimated total memory requirement is approximately 6.42 GB, so it fits within the 8 GB budget, but it leaves less memory headroom than the Mistral configuration.

Qwen3 is therefore a possible alternative, but the additional memory requirement is an important consideration for my 8 GB laptop.

### What Could Change My Recommendation?

If my machine had substantially more available memory, I could consider a larger model or a higher-precision quantization.

If I required a much longer context, the KV cache would become more important and could change which model fits.

If my project required a particular commercial or public redistribution arrangement, I would re-check the exact licence conditions before choosing a model.

If tool calling became a mandatory requirement, I would give additional weight to models whose official documentation explicitly states tool-calling support.

## 7. Conclusion

Choosing an open model requires considering both technical requirements and licence conditions. Model size should be the main deciding factor when the available hardware has limited memory. For example, on an 8 GB laptop, a smaller quantized model may fit while a larger model may not.

Quantization becomes important when a model is close to the available memory limit. Lower-bit quantization can reduce the memory required by the weights, although it may involve a trade-off in model quality.

Context length becomes important for applications that need to process long conversations, documents or accumulated tool results. Increasing the context increases the KV cache requirement even though the model weights remain unchanged.

Licence should be the deciding factor when a model is going to be redistributed, used commercially or released as part of a public project. A model may fit the available hardware but still require additional licence checks before it can be used for a particular purpose.

Therefore, there is no single factor that should always decide the model. Hardware-limited situations require careful attention to model size and quantization, long-context applications require attention to context length and KV-cache growth, and commercial or public projects require careful examination of the exact licence conditions.
