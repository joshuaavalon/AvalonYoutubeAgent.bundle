from log import PlexLog
from show import get_episode_json, get_show_json, set_episode, \
    set_episode_cover, set_show
from utils import convert_date, create_id

version = "1.0.0"


# noinspection PyClassHasNoInit,PyShadowingNames
class AvalonYoutubeTvAgent(Agent.TV_Shows):
    name = "Avalon Rest TV Agent"
    ver = version
    primary_provider = True
    languages = [Locale.Language.NoLanguage]
    accepts_from = ["com.plexapp.agents.localmedia"]

    def search(self, results, media, lang, manual):
        PlexLog.debug("=================== Search Start ===================")

        PlexLog.debug("%s (%s)" % (self.name, self.ver))
        PlexLog.debug("Plex version: %s" % Platform.ServerVersion)

        show = get_show_json(media)
        if show is None:
            return

        title = show.get("title")
        if title is None:
            PlexLog.error("Missing or invalid title: %s" % str(show))
            return

        aired = convert_date(show.get("aired"))
        year = aired.year if aired is not None else 0

        # Plex throws exception that have "/" in ID
        mid = create_id(title, year)
        result = MetadataSearchResult(id=mid,
                                      name=title,
                                      year=year,
                                      lang=lang,
                                      score=100)
        results.Append(result)
        PlexLog.debug("===================  Search end  ===================")

    def update(self, metadata, media, lang, force):
        PlexLog.debug("=================== Update Start ===================")

        PlexLog.debug("%s (%s)" % (self.name, self.ver))
        PlexLog.debug("Plex version: %s" % Platform.ServerVersion)

        show = get_show_json(media)
        if show is None:
            return

        set_show(metadata, show)

        for season in media.seasons:
            for episode in media.seasons[season].episodes:
                episode_metadata = metadata.seasons[season].episodes[episode]
                model = get_episode_json(media, season, episode)
                if model is not None:
                    set_episode(episode_metadata, model)
                set_episode_cover(episode_metadata, media, season, episode)
        PlexLog.debug("===================  Update end  ===================")
