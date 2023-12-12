# Cat Form Order Pizza

This plugin hooks into the CatForm plugin functionality to manage a pizza order

Based on this plugin:
https://github.com/MaxDam/cat-form

<img src="./img/logo.jpg" width=600>

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=383938&style=for-the-badge&logo=cheshire_cat_ai)](https://)  

## Usage

<pre><code>
'''
Prepare the form with field and special class methods
'''
class MyModel(BaseModel):
    field1: str | None = None
    field2: str | None = None
    
    @classmethod
    def get_prompt_examples(cls):
        return [ <json examples> ]
		
	@classmethod
    def prompt_prefix(cls):
        return "<prompt>
		
	@classmethod
    def execute_action(cls, model):
		# execute action
		return "<action output>"
		
</code></pre>

<pre><code>
'''
This hook is used to set the module instance
'''
@hook
def cform_set_model(models, cat):
    return models.append(MyModel())
</code></pre>

<pre><code>
'''
Intent start
'''
@tool(return_direct=True)
def intent_start(model, cat):
	''' <docString> '''

    if "MyModel" in cat.working_memory.keys():
        cform = cat.working_memory["MyModel"]
        return cform.start_conversation()
</code></pre>

<pre><code>
'''
Intent stop
'''
@tool(return_direct=True)
def intent_stop(model, cat):
	''' <docString> '''

    if "MyModel" in cat.working_memory.keys():
        cform = cat.working_memory["MyModel"]
        cform.stop_conversation()    
    return
</code></pre>
