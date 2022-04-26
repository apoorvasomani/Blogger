# Blogger

This is a simple application that enables to create new blog posts.

To run the server -

```python3 manage.py runserver```

These are the API Endpoints -

- Create Blog Post - ```POST 127.0.0.1:8000/posts```
  - Request Body
  ```
  {
    "title": "My First Post",
    "commented_body": {
      "This is my first post. I have ": "",
      "commented": "This is the comment that I have added",
      " the text before. \nI have added a new paragraph as well to this": ""
    }
  }
  ```
  - Response Body
  ```
  {
    "id": 12,
    "title": "My First Post",
    "body": "This is my first post. I have commented the text before. \nI have added a new paragraph as well to this",
    "hash_value": "48b3bcfb-184d-498a-83b5-a8b905838963",
    "commented_body": {
        "This is my first post. I have ": "",
        "commented": "This is the comment that I have added",
        " the text before. \nI have added a new paragraph as well to this": ""
    }
  }
  ```

- Read Blog Post - ```GET 127.0.0.1:8000/posts/12```
  
  - Response Body
  ```
  {
    "id": 12,
    "title": "My First Post",
    "body": "This is my first post. I have commented the text before. \nI have added a new paragraph as well to this",
    "hash_value": "48b3bcfb-184d-498a-83b5-a8b905838963",
    "commented_body": {
        "This is my first post. I have ": "",
        "commented": "This is the comment that I have added",
        " the text before. \nI have added a new paragraph as well to this": ""
    }
  }
  ```

- Update Blog Post - ```PUT 127.0.0.1:8000/posts/<post_id>```
  
  - Request Body
 
 ```
{
    "title": "My First Post",
    "commented_body": {
      "This is the modified blog post. I have ": "",
      "commented": "I have modified the comment as well",
      " the text before. \nI have added a new paragraph as well to this": ""
    }
  }
  
 ```
  
  - Response Body
  
 ```
  {
    "id": 8,
    "title": "My First Post",
    "body": "This is the modified blog post. I have commented the text before. \nI have added a new paragraph as well to this",
    "hash_value": "6966ea60-14fa-43de-92b5-5908df378be9",
    "commented_body": {
        "This is the modified blog post. I have ": "",
        "commented": "I have modified the comment as well",
        " the text before. \nI have added a new paragraph as well to this": ""
    }
}
```


- Delete Blog Post - ```DELETE 127.0.0.1:8000/posts/12```


- Get All Posts - ```GET 127.0.0.1:8000/posts?page=<page_number>```
  - Pagination is enabled on this API. 

- Response Body
  ```
  {
    "count": 10,
    "next": "http://127.0.0.1:8000/posts?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "First Post",
            "body": "This is the \n\nfirst post.",
            "hash_value": "a5717654-41b1-4eb1-833c-db44d43fd3b1",
            "commented_body": {
                "This is ": "",
                "the": "Comment",
                " \n\nfirst post.": ""
            }
        },
        {
            "id": 2,
            "title": "Post 2",
            "body": "This is the \n\nsecond post.",
            "hash_value": "224dc462-e225-4178-b37f-37107981d859",
            "commented_body": {
                "This is ": "",
                "the": "Comment",
                " \n\nsecond post.": ""
            }
        }
    ]
}
```
