<h1 align="center">auto-annotate</h1>

<p align="center">
    </br>
    <img width="100" src="https://github.com/roboflow-ai/notebooks/raw/main/assets/roboflow_logomark_color.svg" alt="roboflow logo">
    </br>
</p>

## 💻 run locally

```console
# clone repository and navigate to root directory
git clone git@github.com:roboflow-ai/auto-annotate.git
cd auto-annotate

# setup python environment and activate it
python3 -m venv venv
source venv/bin/activate

# install
pip install -e .
```

## 🐎 hit the ground running

```console
export ROBOFLOW_API_KEY= ... 
python -m a2.annotate \
--source_image_directory ... \
--target_annotation_directory ... \
--roboflow_project_id ...
--roboflow_project_version ...
```