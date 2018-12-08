# Configuration

## Logging

You can change logging level in Plex agent setting. The default logging level is **INFO**.

You can find the log in `<Plex>/Logs/PMS Plugin Logs/com.plexapp.agents.avalonyoutube.log`

## Customize metadata

You can customize metadata by editing the JSON. Youtube does not provide all the fields to fill in Plex.

### Show

These fields to referring to `items > item[kind=youtube#channel] > brandingSettings > channel`.

| Plex                    | Youtube        | Type                       | Provided |
|-------------------------|----------------|----------------------------|----------|
| Title                   | title          | String                     | Y        |
| Sort Title              | title          | String                     | Y        |
| Content Rating          | content_rating | String                     | N        |
| Studio                  | studio         | String                     | N        |
| Originally Available At | aired          | String (`YYYYMMDD`)        | N        |
| Summary                 | description    | String                     | Y        |
| Rating                  | rating         | Float (0 ~ 10)             | N        |
| Genres                  | keywords       | String (Split by space)    | Y        |
| Collections             | collections    | List of string             | N        |
| Actors                  | actors         | Object (name, role, photo) | N        |

Note that `actors` is a JSON object and `photo` is the url of the image (Not path).

You can see an [example](./example.md#show).

### Episode

These fields to referring to root level of the JSON.

| Plex                    | Youtube        | Type                | Provided |
|-------------------------|----------------|---------------------|----------|
| Title                   | title          | String              | Y        |
| Originally Available At | upload_date    | String (`YYYYMMDD`) | Y        |
| Summary                 | description    | String              | Y        |
| Rating                  | average_rating | Float (0 ~ 10) * 2  | Y        |
| Writers                 | writers        | List of string      | N        |
| Directors               | directors      | List of string      | N        |

You can see an [example](./example.md#episode).
