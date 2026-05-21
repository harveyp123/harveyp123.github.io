---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

1. [Efficient machine learning systems](#mlsys)
2. [Secure and Trustworthy AI/ML systems](#ai)


## Efficient machine learning systems <a name="mlsys"></a>
My current research focuses on efficient algorithm design and mapping on existing computing platforms such as FPGA and GPU. [Medusa](https://sites.google.com/view/medusa-llm) is a easy-to-use framework which accelerates LLM generation through multiple light-weighted decoding head. The overhead is much smaller than that of the draft model based speculative decoding design. 
My [DAC22](https://arxiv.org/pdf/2208.03646) paper is a Transformer-based model mapping on FPGA which features sequence-length adaptive hardware design and re-designed linear complexity self-attention. My [ICCAD23](https://arxiv.org/abs/2308.11825) paper is a GNN mapping on GPU which features degree sorting, block-level partition and combined warp on GPU CUDA kernel, which maximizes GPU memory bandwidth and computational parallelism on SpMM operator. 

### **Featured open source project**
- [Medusa: Simple Framework for Accelerating LLM Generation with Multiple Decoding Heads](https://sites.google.com/view/medusa-llm), 2023. \[[Code](https://github.com/FasterDecoding/Medusa)\].

### **Featured publications**
- [Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models](/paper_blogs/complete_mue/) (**Preprint**), 2025. \[[Blog](/paper_blogs/complete_mue/)\].
- [MaxK-GNN: Towards Theoretical Speed Limits for Accelerating Graph Neural Networks Training](https://arxiv.org/abs/2312.08656)  (**ASPLOS**), 2024. \[[Code](https://github.com/harveyp123/MaxK-GNN)\].
- [Accel-GCN: High-Performance GPU Accelerator Design for Graph Convolution Networks](https://arxiv.org/abs/2308.11825)  (**ICCAD**), 2023. \[[Code](https://github.com/xiexi1990/iccad-accel-gnn)\].
- [A length adaptive algorithm-hardware co-design of transformer on fpga through sparse attention and dynamic pipelining](https://arxiv.org/pdf/2208.03646) (**DAC**), 2022, **publicity paper**!.
- [Towards sparsification of graph neural networks](https://arxiv.org/pdf/2208.03646) (**ICCD**), 20022. \[[Code](https://github.com/harveyp123/ICCD_SpTrn_SLR)\].

<br>

## Secure and Trustworthy AI/ML systems <a name="ai"></a>

My current research focuses on novel algorithms and hardware co-design for accelerating privacy-preserving machine learning, aiming to facilitate the practical deployment of PPML across various industries that interact with sensitive data, such as healthcare, biomedicine, banking, finance, etc.

### **Featured publications**
- [LinGCN: Structural Linearized Graph Convolutional Network for Homomorphically Encrypted Inference](http://arxiv.org/abs/2309.14331) (**NeurIPS**), 2023. \[[Code](https://github.com/harveyp123/LinGCN-Neurips23)\].
- [AQ2PNN: Enabling Two-party Privacy-Preserving Deep Neural Network Inference with Adaptive Quantization](https://dl.acm.org/doi/10.1145/3613424.3614297)(**MICRO**), 2023. 
- [AutoReP: Automatic ReLU Replacement for Fast Private Network Inference](#) (**ICCV**), 2023. \[[Code](https://github.com/harveyp123/AutoReP)\].
- [PASNet: Polynomial Architecture Search Framework for Two-party Computation-based Secure Neural Network Deployment](https://arxiv.org/pdf/2306.15513) (**DAC**), 2023. \[[Code](https://github.com/HarveyP123/PASNet-DAC2023)\].

<br>