
# SINU Admissions Portal

This application facilitates student submissions for program enrollment at the Solomon Islands National University (SINU).


## Features

- Course Search & Selection
- Application creation based on selected course
- User Authentication
- Student/Staff Dashboard (work on application at own pace)
- Application Status Monitoring
- Advanced Filtering of submitted applications by Staff (e.g. by faculty/school)
- Report/Analysis of all submissions


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
GET /admissions/new-application/?course_code=[code]
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `code`      | `string` | **Required**. required for POST request |

returns new application form.


#### Submit Application Form

```http
POST /admissions/new-application/?course_code=[code]
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `code`      | `string` | **Required**. creates new application for course |

- creates new user account.
- creates new application for specified course, for new user.

#### Get admission application draft (User Authentication Required)

```http
GET /admissions/application/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. id of application in draft |

Returns application if it is in DRAFT and belongs to authenticated user.


#### Get User Dashboard (User Authentication Required)

```http
GET /dashboard
```

Returns user dashboard depending on user type (e.g. staff, student).


## Future Roadmap

- Integrate a React and Next.js frontend as part of the application.
- Refactor the current app into Django REST APIs to handle requests from the frontend.

