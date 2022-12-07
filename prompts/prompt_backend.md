# Backend Engineer Prompt

We'd like to start a web app named Anaconda Eats, where employees can share recipes with each other!

### Your task:
* Create an API for interactions between the web app and the database. Your API should be able to:
    - Create a recipe.
    - Retrieve a list of all recipes (or a single recipe)
    - Edit an existing recipe.
    - Delete an existing recipe.

Here's what an example Recipe model might look like:
```
Recipe:
	Title: string
	Ingredients: [{
		Ingredient: string,
		Quantity: string
	}]
	Instructions: string
	Thumbnail: string (file URL)
	Cook time: IsoString
	Prep time: IsoString
	Total time: IsoString
	Serving size: string
```

### Tips
* Please reach out to your interviewer with any clarifying questions before getting started.
* Documentation is essential! Tell or show us how your API should be used.
* Feel free to use any language and/or framework you are comfortable with.
* You don't need to set up a database, you can use a simple list or json file. Do feel free to hook up your API to a database if you have extra time, though!
* Testing is important! Tell or show us how you would test your API once it is complete.

