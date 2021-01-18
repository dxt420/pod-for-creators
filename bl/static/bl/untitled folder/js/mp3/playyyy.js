var adonisPlaylist, currentPlaylistId, playSong, adonisPlayer = {},
    adonisAllPlaylists = [],
    adonisPlayerID = "adonis_jplayer_main",
    adonisPlayerContainer = "adonis_jp_container";
jQuery(document).ready(function (a) {
    "use strict";
    adonisPlayer.init = function () {
        function e(a) {
            var e = /{(.*?\})/,
                t = a.replace(e, ""),
                i = a.match(e, "");
            if (null != i) var s = i[1].replace("}", "");
            return {
                link: s,
                name: t
            }
        }
        adonisPlaylist = new adonisJPlayerPlaylist({
            jPlayer: "#" + adonisPlayerID,
            cssSelectorAncestor: "#" + adonisPlayerContainer
        },  {
            playlistOptions: {
                enableRemoveControls: !0
            },
            swfPath: "/js",
            supplied: "oga, mp3",
            useStateClassSkin: !0,
            autoBlur: !1,
            smoothPlayBar: !1,
            keyEnabled: !1,
            audioFullScreen: !0,
            display: !1,
            autoPlay: !1
        }), a("#" + adonisPlayerID).bind(a.jPlayer.event.loadeddata, function (t) {
            e(a(this).data("jPlayer").status.media.artist);
            var i = a(this).data("jPlayer").status.media.poster;
            a(this).data("jPlayer").status.media.title, a("#" + adonisPlayerContainer + " .current-item .song-poster img").attr("src", i), a("#" + adonisPlayerID).find("img").attr("alt", "")
        }), a(document).on("click", "#adonis-playlist .playlist-item .song-poster", function () {
            a(this).parent().find(".jp-playlist-item").trigger("click")
        }), a("#" + adonisPlayerID).bind(a.jPlayer.event.play + ".jp-repeat", function (t) {
            var i = a(this).data("jPlayer").status.media.poster;
            a("#" + adonisPlayerContainer).find(".adonis-player .song-poster img").attr("src", i), a("#" + adonisPlayerContainer).find(".blurred-bg").css("background-image", "url(" + i + ")");
            var s = e(a(this).data("jPlayer").status.media.artist);
            s.name ? a("#" + adonisPlayerContainer + " .artist-name").html('<a href="' + s.link + '">' + s.name + "</a>") : a("#" + adonisPlayerContainer + " .artist-name").html(s.name), void 0 !== currentPlaylistId && a("[data-album-id='" + currentPlaylistId + "']").addClass("jp-playing")
        }), a(".adonis-mute-control").click(function () {
            var e = a(this);
            if (e.hasClass("muted")) {
                var t = e.attr("data-volume");
                a("#" + adonisPlayerID).jPlayer("unmute"), e.removeClass("muted"), a("#" + adonisPlayerID).jPlayer("volume", t)
            } else t = a("#" + adonisPlayerID).data("jPlayer").options.volume, e.attr("data-volume", t), a("#" + adonisPlayerID).jPlayer("mute").addClass("muted"), e.addClass("muted")
        }), a("#" + adonisPlayerID).bind(a.jPlayer.event.pause + ".jp-repeat", function (e) {
            void 0 !== currentPlaylistId && a("[data-album-id='" + currentPlaylistId + "']").removeClass("jp-playing")
        });
        var t = !1;
        a(".jp-progress").mousedown(function (e) {
            t = !0;
            var o = s(e.pageX, a(this));
            a(this).addClass("dragActive"), i(o)
        }), a(document).mouseup(function (e) {
            if (t) {
                t = !1;
                var o = s(e.pageX, a(".jp-progress.dragActive"));
                a(".jp-progress.dragActive"), o && (a(".jp-progress.dragActive").removeClass("dragActive"), i(o))
            }
        }), a(document).mousemove(function (e) {
            if (t) {
                var o = s(e.pageX, a(".jp-progress.dragActive"));
                i(o)
            }
        });
        var i = function (e) {
            var t = a("#" + adonisPlayerID).jPlayer.duration;
            return a(".jp-play-bar").css("width", e + "%"), a("#" + adonisPlayerID).jPlayer("playHead", e), a("#" + adonisPlayerID).jPlayer.currentTime = t * e / 100, !1
        };

        function s(e, t) {
            var i = t,
                s = (a("#" + adonisPlayerID).jPlayer.duration, 100 * (e - i.offset().left) / i.width());
            return s > 100 && (s = 100), s < 0 && (s = 0), s
        }
        var o = !1;
        a(document).on("mousedown", ".jp-volume-bar", function (a) {
            o = !0, l(a.pageX)
        }), a(document).mouseup(function (a) {
            o && (o = !1, l(a.pageX))
        }), a(document).mousemove(function (a) {
            o && l(a.pageX)
        });
        var l = function (e) {
            var t = a(".jp-volume-bar"),
                i = 100 * (e - t.offset().left) / t.width();
            i > 100 && (i = 100), i < 0 && (i = 0), a("#" + adonisPlayerID).jPlayer("volume", i / 100)
        };
        a(document).on("click", ".remove-track-item-playlist", function () {
            var a = openMenu.parents("li.item");
            adonisPlaylist.remove(a.length - 1)
        }), a(document).on("click", ".remove-track-item-current", function () {
            adonisPlaylist.remove(adonisPlaylist.current)
        }), adonisPlayer.addTrack = function (a) {
            var e, t = tracks[a],
                i = !1;
            return adonisPlaylist.playlist.forEach(function (t, s) {
                t.id == a && (i = !0, e = s)
            }), !1 === i && (adonisPlaylist.add(t), e = adonisPlaylist.playlist.length - 1), e
        }, adonisPlayer.transferAlbum = function (e) {
            a(document).on("click", e, function (e) {
                e.preventDefault();
                var t = a(this).attr("data-poster-target"),
                    i = a(this).attr("data-poster"),
                    s = a(this).attr("data-track"),
                    o = a(t).clone();
                o.css("background-image", "url(" + i + ")").fadeOut(0), o.insertAfter(a(t)), a(t).fadeOut("slow", function () {
                    a(this).remove()
                }), o.fadeIn("slow");
                var l = adonisPlayer.addTrack(s);
                adonisPlaylist.play(l)
            })
        }, adonisPlayer.transferAlbum(".transfer-album"), a(document).on("click", ".adonis-album-button", function (e) {
            var t = parseInt(a(this).attr("data-album-id"));
            t && void 0 !== adonisAllPlaylists[t] && currentPlaylistId !== t && (adonisPlaylist.setPlaylist(adonisAllPlaylists[t]), currentPlaylistId = t), a("#" + adonisPlayerID).data().jPlayer.status.paused ? setTimeout(function () {
                adonisPlaylist.play(0)
            }, 700) : adonisPlaylist.pause()
        }), adonisPlayer.addPlaylist = function (a) {
            a && void 0 !== adonisAllPlaylists[a] && adonisAllPlaylists[a].forEach(function (a) {
                adonisPlaylist.add(a)
            })
        }
    }, a(window).imagesLoaded(function () {
        setTimeout(function () {
            adonisPlayer.init()
        }, 100), setTimeout(function () {
            adonisPlaylist.setPlaylist(adonisAllPlaylists[0])
        }, 5e3)
    }), playSong = function (title,artist,cover,song) {
    
        adonisAllPlaylists[0] = [{
            title: "title",
            artist: "artist",
            mp3: "song",
            poster: "cover"
        }], adonisPlaylist.play(0), console.log(adonisPlaylist), console.log(adonisAllPlaylists)
    }
});