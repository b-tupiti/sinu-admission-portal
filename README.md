## URL Reference

#### Search for course(s)

```http
  GET /?search=[input]
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `search` | `string` | **Optional**. filters by course name, title, or code. |

returns a list of courses from filtered parameter.

#### Fetch course by course code

```http
  GET /course-detail/<code>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `code`      | `string` | **Required**. course code of course to fetch |

returns course and corresponding details.


#### Get admission Application Form based on course

```http
GET admission/new-application/?course_code=[code]
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `code`      | `string` | **Required**. required for POST request |

returns new application form.


#### Submit Application Form

```http
POST admission/new-application/?course_code=[code]
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `code`      | `string` | **Required**. creates new application for course |

- creates new user account.
- creates new application for specified course, for new user.

#### Get admission application draft (User Authentication Required)

```http
GET admissions/application/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. id of application in draft |

Returns application if it is in DRAFT and belongs to authenticated user.
