# y2mapi
unofficial y2mate API's

# Check Resolution Video API
* URL: ```https://nuubi.herokuapp.com/api/y2mate/check_reso/<type>?```
* Data: ```url=<youtube_url>```
* Methods: ```GET``` or ```POST```
> example for GET request: https://nuubi.herokuapp.com/api/y2mate/check_reso/mp4?url=https://www.youtube.com/watch?v=x3bfa3DZ8JM

# URL Download Video API
* URL: ```https://nuubi.herokuapp.com/api/y2mate/download/<type>?```
* Data: ```url=<youtube_url>&quality=<video_quality>```
* Methods: ```GET``` or ```POST```
> example for GET request: https://nuubi.herokuapp.com/api/y2mate/check_reso/mp4?url=https://www.youtube.com/watch?v=x3bfa3DZ8JM&quality=720p

* Example Used: <a href="https://github.com/KANG-NEWBIE/y2mapi/blob/master/y2mate-dl.py">Source Code</a>
