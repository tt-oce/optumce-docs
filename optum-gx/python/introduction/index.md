# Introduction

The OPTUM GX Python interface enables straightforward scripting control of geotechnical models, analyses, and results.

Instead of building models manually through the graphical interface, Python allows you to define geometry, materials, loads, and analysis settings directly in code. This approach enables automation, reproducibility, and scalable workflows.

---

## Why Use Python in GX?

Python scripting is designed for engineers who want more control and efficiency:

* Automate repetitive tasks and reduce manual input
* Ensure consistency across analyses
* Perform parametric studies efficiently
* Extract and process results in one go
* Build custom tools and plugins

### Manual vs Python Workflow

| Manual GX                | Python GX                     |
| ------------------------ | ----------------------------- |
| GUI-based modelling      | Script-based modelling        |
| One model at a time      | Parametric creation           |
| Manual result extraction | Automated data extraction     |
| Repetitive work          | Reusable scripts              |

---

## When to Use Python

Python is especially useful when:

* You need to run multiple similar analyses
* You want reproducible and version-controlled workflows
* You are integrating GX into a larger pipeline
* You are building internal engineering tools
* You want to assess geotechnical performance probabilistically

---

## How It Works

A typical GX Python workflow consists of:

1. Creating a project
2. Defining the model (geometry, materials, loads, supports, features)
3. Configuring analysis settings
4. Running the analysis
5. Extracting and processing results

The Python interface mirrors the structure of GX, making it intuitive to move from manual modelling to scripting. The transition is simplified by the option to auto-generate python code from your GX projects.  
It may help your intuitive understanding to think of the mouse clicks you are used to making in GX, as separate coordinate inputs in Python functions.

## Recommended Learning Path

To get started effectively:

1. Introduction (this page)
2. Environment setup
3. First complete model script
4. Examples
5. Python function reference

---

## GX Object and Scripting Structure

Understanding the structure of GX is key to using the Applicaiton Programming Interface (API) effectively:

```text
GX Application
  └── Project
        ├── Materials
        └── Model
              ├── Geometry
              ├── Loads
              └── Analysis Settings
```
This hierarchy is reflected directly in the Python interface member functions.

All Python scripts will start with importing the OptumGX library, which allows you to interact directly with the GX application, subsequently the GX hierachy is followed to create the objects needed:

```python
from OptumGX import *

gx = GX()                                       # GX Application
prj = gx.create_project("MyFirstProject")       # Project
m = prj.get_model()[0]                          # Model (default model)
```
From here, you can begin adding geometry, materials, features and analyses. Before we get in to modelling, a brief overview of where everything lives in the GX hierachy is presented, in order to provide you with the best foundation for applying the GX Python functions.  
The GX application level only has a handful of functions, with the main functionality being creating, opening and saving projects.  
The Project level primarily contains materials creation functions, but it also includes coordinate systems, model operations and running analyses. All these are hence members functions of the project object.
The Model level contains functions for modifying geometry and features as well as stage operations.

<div style="border: 2px solid rgb(19, 9, 9); padding: 10px; border-radius: 6px; background-color: #ffecec;">
  <strong>📖 Optional context:</strong><br>
  One thing to note is that a number of functions are members of both stage and model. This is rooted in the choise that a model with no explicitly created stages should still available for analysis, hence it essentially behaves as an implicit stage. 
</div>



The next step is for to apply all this by by creating your first script.  
Be sure that your Integrated Development Environment (IDE) is configured properly. We recommend using either of the IDE's Visual Studio Code or Spyder for Python scripting, which can be set up using the following guides: [Setting up VS Code](../setting-up-ide/vs-code.md) & [Setting up Spyder](../setting-up-ide/spyder.md)
---


<!-- ## Suggested Visuals (to add in site) -->

<!--
1. Diagram:
   GX Object Model (Application → Project → Model)

2. Workflow pipeline graphic

3. Comparison table (Manual vs Python) as visual cards
-->

---
<!-- 
## Next Step

Continue to the setup and examples to start building your first automated GX workflows. -->

---
