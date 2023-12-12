# Cat Form Order Pizza

This plugin hooks into the CatForm plugin functionality to manage a pizza order

Based on this plugin:
https://github.com/MaxDam/cat-form

<img src="./img/logo.jpg" width=600>

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=383938&style=for-the-badge&logo=cheshire_cat_ai)](https://)  

## Usage

<pre><code>
'''
Prepare the form
'''
class MyModel(BaseModel):
    field1: str | None = None
    field2: str | None = None
    
    @classmethod
    def get_prompt_examples(cls):
        return [ <json examples> ]
</code></pre>

<pre><code>
'''
This hook is used to set the module instance
'''
@hook
def cform_set_model(model, cat):
    return MyModel()
</code></pre>

<pre><code>
'''
This hook allows you to manipulate the 
prompt to request missing information
'''
@hook
def cform_ask_missing_information(prompt, cat):
	# ......
    return prompt
</code></pre>
	
<pre><code>
'''
This hook allows you to manipulate 
the prompt to ask for user confirmation
'''
@hook
def cform_show_summary(prompt, cat):
	# ......
    return prompt
</code></pre>

<pre><code>
'''
This Hook is called when the form is filled out 
and user confirmation is obtained
'''
@hook
def cform_execute_action(model, cat):
    # ......
	return result
</code></pre>
