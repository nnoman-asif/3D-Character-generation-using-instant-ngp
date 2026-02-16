<p align="center">
  <img src="FYP_web/src/assets/logo.png" width="200" alt="3C Logo">
</p>

<h1 align="center">



3D Character Generation using Instant-NGP</h1>

<p align="center">
  A desktop application that generates textured 3D character models from a single video using Neural Radiance Fields (NeRF).<br>
  Built as a Final Year Project (FYP) at FAST NUCES.
</p>

## Demo

<p align="center">
  https://github.com/user-attachments/assets/7eb7fb19-000d-4aef-8606-145598f4f10a
</p>

## Overview

3C simplifies the process of creating 3D characters for game engines like Unreal Engine. Instead of manual modeling, users provide a 360-degree video of a subject, and the application handles the entire pipeline:

**Video** &rarr; **Frame Extraction** &rarr; **Background Removal** &rarr; **Optional Cartoonization** &rarr; **NeRF 3D Reconstruction** &rarr; **Mesh Texturing** &rarr; **3D Model**

| Folder | Description |
|---|---|
| `3C_App/` | PyQt5 desktop application — the main tool with the full processing pipeline |
| `FYP_web/` | React website — promotional site with project info and app download |

## Desktop Application Setup

### Prerequisites

The following external tools must be installed and accessible on your system:

1. **COLMAP** - Structure-from-Motion and Multi-View Stereo
   - Download: https://colmap.github.io/install.html
   - Required for extracting camera poses from video frames

2. **NVIDIA Instant-NGP** - Neural Radiance Fields
   - Download: https://github.com/NVlabs/instant-ngp
   - Required for 3D scene reconstruction from images
   - Requires an NVIDIA GPU with CUDA support

3. **COLMAP2NeRF script** (`colmap2nerf.py`)
   - Included with Instant-NGP
   - Converts COLMAP output to NeRF-compatible format

### Model Weights

All pretrained model weights are included in the repository:

- **IS-Net** (`isnet.pth`) — located at `3C_App/isNetModel/saved_models/`
  - Source: [DIS (Dichotomous Image Segmentation)](https://github.com/xuebinqin/DIS)
- **Cartoonizer** (`model-33999.*`) — located at `3C_App/Cartoonizer/saved_models/`
  - Source: [White-box Cartoonization](https://github.com/SystemErrorWang/White-box-Cartoonization)

> **Note:** Large files (`.pth`, `.zip`, `.mp4`) are stored using [Git LFS](https://git-lfs.github.com/). Make sure Git LFS is installed before cloning: `git lfs install`

### Installation

```bash
cd 3C_App
pip install -r requirements.txt
```

### Running

```bash
cd 3C_App
python main.py
```

### Application Workflow

1. **Create Project** - Name your project; folder structure is created automatically
2. **Step 1** - Select AABB scale and video FPS, then provide your 360-degree video
3. **Step 2** - Choose Human or Object mode for background removal
4. **Step 3** - Optionally cartoonize the extracted frames
5. **Step 4** - Launch Instant-NGP to generate the NeRF, then export and texture the mesh

## Website

The website is a React SPA that showcases the 3C project and provides a download link for the desktop application.

```bash
cd FYP_web
npm install
npm start
```

The site runs at `http://localhost:3000`.

## Technology Stack

| Component | Technology |
|---|---|
| Desktop UI | PyQt5 |
| Background Removal | IS-Net (PyTorch), rembg |
| Cartoonization | TensorFlow (U-Net + Guided Filter) |
| 3D Reconstruction | NVIDIA Instant-NGP, COLMAP |
| Mesh Processing | PyMeshLab, Open3D |
| Web Frontend | React, React Router |

## Team

- **Noman Asif** - [LinkedIn](https://www.linkedin.com/in/noman-asif-682085270)
- **Afaq Qureshi** - [LinkedIn](https://www.linkedin.com/in/afaq-qureshi-a92463251/)
- **Faizan Zubair** - [LinkedIn](https://www.linkedin.com/in/faizan-satti-112a9b233/)
