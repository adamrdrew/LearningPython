import { createStore } from 'vuex'

// Create a new store instance.
const store = createStore({
  state () {
    return {
      PlayQueue: [],
      NowPlayingIndex: 0,
    }
  },
  mutations: {
    SkipForward (state) {
        if ( !this.getters.CanSkipForward ) return;
        state.NowPlayingIndex++;
    },
    SkipBackward (state) {
        if ( state.NowPlayingIndex == 0 ) return;
        state.NowPlayingIndex--;
    },
    SetPlayQueue(state, queue) {
        state.PlayQueue = queue;
    },
    AddToPlayQueue(state, song) {
        state.PlayQueue.push(song);
    },
    ClearPlayQueue(state) {
        state.PlayQueue = [];
    }
  },
  getters: {
      NowPlayingSong(state) {
          return state.PlayQueue[state.NowPlayingIndex] || {
            ID: 0,
            Title: "",
            ArtSmall: "",
            ArtLage: ""
          };
      },
      CanSkipForward(state, getters) {
          return state.NowPlayingIndex < getters.PlayQueueLength - 1;
      },
      CanSkipBackward(state) {
        return state.NowPlayingIndex > 0;
      },
      PlayQueueLength(state) {
          return state.PlayQueue.length;
      }
  },
  actions: {
    async GetAndQueueAlbumSongs(context, AlbumID) {
      const res = await fetch("http://127.0.0.1:5000/api/album/" + AlbumID);
      const d = await res.json();
      context.commit('SetPlayQueue', d.songs);
    },
    async GetAndQueueSong(context, SongID) {
      const url = "http://127.0.0.1:5000/api/song/" + SongID;
      const res = await fetch(url);
      const d = await res.json();
      context.commit('SetPlayQueue', [d]);
    }
  }
})

export default store;
