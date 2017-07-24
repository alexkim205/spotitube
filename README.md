# Spotitube
A lightweight tool that downloads tracks in any Spotify playlist to local Music folder as mp3 files.

## A Short Description
**spotitube** is a command-line program to download mp3 files of tracks in user Spotify playlists. It is not platform specific, and will run on Mac OS X, Windows, and Linux. It is released on public domain, so you can modify, redistribute, and use freely.

## Prerequisites

What things you need to install the software and how to install them

#### [youtube_dl](https://github.com/rg3/youtube-dl)
```
youtube_dl >= 2017.7.23
$ sudo -H pip install --upgrade youtube-dl
```
#### requests
```
requests >= 2.11.0
$ pip install requests
```

#### [spotipy](https://github.com/plamere/spotipy)
```
spotipy >= 2.4.4
$ pip install spotipy
```

#### [eyeD3](https://github.com/nicfit/eyeD3)
```
eyeD3 >= 0.8
$ pip install eyeD3
```

#### [google_api_python_client]()
```
google_api_python_client >= 1.6.2
$ pip install --upgrade google-api-python-client
```

## Quick Start

```
$ python spotify.py -h
usage: spotify.py [-h] [-c CLIENT] [-cs CLIENT_SECRET] [-u URI]

required arguments:
  -c, --client            Spotify client key
  -cs, --client-secret    Spotify client secret key
  -u, --uri               Spotify playlist URI

optional arguments:
  -h, --help              show this help message and exit
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
