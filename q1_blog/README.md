# Examples of Post CRUD APIs

## GET

* GET http://127.0.0.1:8000/api/posts  
* GET http://127.0.0.1:8000/api/posts/3

## POST

* POST http://127.0.0.1:8000/api/posts/
<pre>
{
	"user_id": 1,
	"title": "Title",
	"content": "Content"
}
</pre>

## PUT

* PUT http://127.0.0.1:8000/api/posts/3/
<pre>
{
	"title": "New Title"
}
</pre>

* PUT http://127.0.0.1:8000/api/posts/3/
<pre>
{
	"content": "New Content"
}
</pre>


## DELETE

* DELETE http://127.0.0.1:8000/api/posts/20