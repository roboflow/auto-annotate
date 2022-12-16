<h1 align="center">auto-annotate</h1>

<p align="center">
    </br>
    <img width="100" src="https://github.com/roboflow-ai/notebooks/raw/main/assets/roboflow_logomark_color.svg" alt="roboflow logo">
    </br>
</p>

## 💻 run locally

Remember don't install your dependencies globally, use
[venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

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

## 🏃 hit the ground running

> **Warning**
> Your `ROBOFLOW_API_KEY` is the secret. Do not commit it to your repository, especially if it is public.

```console
export ROBOFLOW_API_KEY= ... 
python -m a2.annotate \
--source_image_directory ... \
--target_annotation_directory ... \
--roboflow_project_id ... \
--roboflow_project_version ...
```

## 🪄 label assist

auto-annotate is perfect if you want to automatically label large batches of data fast. However, if you prefare more control over what detections fall into your dataset, you can use [Label Assist](https://blog.roboflow.com/announcing-label-assist/) in our web interface. You will use the same pre-trained model, but have the ability to correct AI suggestions on the fly.

![Screen Recording 2022-12-16 at 17 14 12](https://user-images.githubusercontent.com/26109316/208144936-047e8a67-86ec-41ee-8b1a-12877f48118e.gif)
