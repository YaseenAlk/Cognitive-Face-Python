# face_api_helper: Implementing ROS [face_msgs](https://github.com/YaseenAlk/face_msgs) into Microsoft's [Cognitive-Face-Python](https://github.com/Microsoft/Cognitive-Face-Python) SDK.
This branch can be used as a git submodule for python projects that need to use Microsoft's Face API. 

Additionally, I've implemented ROS messages for Face API's HTTP requests and responses.

## Using this branch:

### Adding the branch as a submodule
In your repository of interest, run the following commands:
```shell
git submodule add -b ROS-implementation https://github.com/YaseenAlk/Cognitive-Face-Python.git <path>
```
where `<path>` is the directory to put the submodule into.

This command clones the `ROS-implementation` branch from the specified remote URL, `https://github.com/YaseenAlk/Cognitive-Face-Python.git`.

Next, we need to initialize the submodule:
```shell
git submodule update --init --recursive
```

Finally, we can fetch and apply submodule updates using the following command:
```shell
git submodule update --remote --recursive
```

It's important to include the `--recursive` arg, because this submodule has a submodule within it.

For more information on git submodules, check out this [third-party guide](https://www.activestate.com/blog/2014/05/getting-git-submodule-track-branch), this [guide](https://git-scm.com/book/en/v2/Git-Tools-Submodules) made by the documenters of git, and of course, the [official git documentation](https://git-scm.com/docs/git-submodule).

### Using this submodule
```python
import <path>.face_api_helper as helper

KEY = 'subscription key'  # Replace with a valid Subscription Key here.
helper.Key.set(KEY)

BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
helper.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = helper.face.detect(img_url)
print result

# Access wrappers for FaceAPIRequest and FaceAPIResponse (part of face_msgs ROS package)
request_msg_wrapper = helper.MostRecentRequest.get()
response_msg_wrapper = helper.MostRecentResponse.get()
```

### Adding api_access_key.txt
Another way to initialize the helper is to include a file called `api_access_key.txt` somewhere in the repo folder. It should contain the following inside:
``` json
{
	"subscriptionKey":"<subkey>",
	"uriBase":"https://[location].api.cognitive.microsoft.com/face/v1.0/"
}
```
where `<subkey>` is your API subscription key and `[location]` is the region (e.g. westcentralus, eastus, ...).

Then, in the above excerpt, you can replace these lines:
``` python
KEY = 'subscription key'  # Replace with a valid Subscription Key here.
helper.Key.set(KEY)

BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
helper.BaseUrl.set(BASE_URL)
```

with this snippet:
``` python
with open(API_ACCESS_KEY_LOC, "r") as f:             # load api_access_key json
    api_access_key = f.read()                        
helper.util.init_from_json_str(api_access_key)       # initialize helper
```

where `API_ACCESS_KEY_LOC` is the file path for the `api_access_key.txt` file.

Original README below:
---
# Microsoft Face API: Python SDK & Sample
This repo contains the Python SDK for the Microsoft Face API, an offering within [Microsoft Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/), formerly known as Project Oxford.

* [Learn about the Face API](https://azure.microsoft.com/en-us/services/cognitive-services/face/)
* [Documentation & API Reference & SDKs](https://docs.microsoft.com/en-us/azure/cognitive-services/face/)

## Getting started

Install the module using [pip](https://pypi.python.org/pypi/pip/):

```bash
pip install cognitive_face
```

Use it:

```python
import cognitive_face as CF

KEY = 'subscription key'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print result
```

### Installing from the source code

```bash
python setup.py install
```

### Running the unit tests

To run the tests you will need a valid subscription. You can get one [here](https://azure.microsoft.com/en-us/try/cognitive-services/?api=face-api).

1. Copy `cognitive_face/tests/config.sample.py`  into `cognitive_face/tests/config.py`.
1. Change the `KEY` and `BASE_URL` parameters to your own subscription's API key and endpoint.
1. Run the following:

```bash
python setup.py test
```

## Running the sample

A sample desktop application is also provided.

Currently it support the following combination of prerequisites:

1. [Python 3](https://www.python.org/downloads/) + [wxPython 4](https://pypi.python.org/pypi/wxPython) **[Recommended]**
1. [Python 2](https://www.python.org/downloads/) + [wxPython 4](https://pypi.python.org/pypi/wxPython)
1. [Python 2](https://www.python.org/downloads/) + [wxPython 3](https://sourceforge.net/projects/wxpython/files/wxPython/3.0.2.0/)

P.S. WxPython 3 does not support Python 3 by design.

Then run the following:

```bash
git clone https://github.com/Microsoft/Cognitive-Face-Python.git
cd Cognitive-Face-Python
pip install -r requirements.txt
python sample
```

![Sample app](./Assets/sample_screenshot.png)


## Contributing

We welcome contributions. Feel free to file issues and pull requests on the repo and we'll address them as we can. Learn more about how you can help on our [Contribution Rules & Guidelines](/CONTRIBUTING.md).

You can reach out to us anytime with questions and suggestions using our communities below:
 - **Support questions:** [StackOverflow](https://stackoverflow.com/questions/tagged/microsoft-cognitive)
 - **Feedback & feature requests:** [Cognitive Services UserVoice Forum](https://cognitive.uservoice.com)

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Updates
* [Face API Release Notes](https://docs.microsoft.com/en-us/azure/cognitive-services/face/releasenotes)

## License
All Microsoft Cognitive Services SDKs and samples are licensed with the MIT License. For more details, see
[LICENSE](/LICENSE.md).

Sample images are licensed separately, please refer to [LICENSE-IMAGE](/LICENSE-IMAGE.md).

## Developer Code of Conduct
Developers using Cognitive Services, including this sample, are expected to follow the “Developer Code of Conduct for Microsoft Cognitive Services”, found at [http://go.microsoft.com/fwlink/?LinkId=698895](http://go.microsoft.com/fwlink/?LinkId=698895).
