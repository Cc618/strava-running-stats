# Strava Running Statistics

Script to fetch data from your activities on Strava and display various statistics from them.

:run:

## Example

```
Fetching activities
Page 1
Page 2
Page 3
Page 4
Page 5
Page 6
Page 7
Page 8

110 activities
Raw data:
          distance          time      pace
              mean          mean      mean count
kind
5      5070.076471   1586.147059  5.219040    34
10    10094.208000   3142.120000  5.188047    50
15    15118.290909   4945.454545  5.432244    11
20    20500.008333   7153.666667  5.902428    12
30    30015.700000   9232.000000  5.126210     2
40    42217.700000  15613.000000  6.163686     1

Summary:
-  5K: 5:13min/km (11.5km/h) (34 activities)
- 10K: 5:11min/km (11.6km/h) (50 activities)
- 15K: 5:25min/km (11.0km/h) (11 activities)
- 20K: 5:54min/km (10.2km/h) (12 activities)
- 30K: 5:07min/km (11.7km/h) (2 activities)
- 40K: 6:09min/km (9.7km/h) (1 activities)
```

## Usage

### API Token

You need to have an API access code from Strava, for this go to https://www.strava.com/settings/api.

Then, you need to have an access token by doing OAuth2 :

1. Go to : `http://www.strava.com/oauth/authorize?client_id=$client_id&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read,activity:read` (replace $client_id)
2. Find the `code` argument after being redirected
3. Get a token using this command :
    ```sh
    curl -X POST https://www.strava.com/api/v3/oauth/token \
    -d client_id="$client_id" \
    -d client_secret="$client_secret" \
    -d code="$code" \
    -d grant_type=authorization_code
    ```
4. Export the token :
    ```sh
    export STRAVA_API_KEY="$access_token"
    ```

### Main script

The main script will do everything for you.

```sh
python3 main.py
```

### Customization

Feel free to change `max_pages` within `main.py` to fetch more recent data (a page is about 30 activities, by default it fetches the last 600 activities).
