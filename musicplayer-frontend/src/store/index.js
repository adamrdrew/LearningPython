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
        if ( !state.CanSkipForward ) return;
        state.NowPlayingIndex++;
    },
    SkipBackward (state) {
        if ( !state.CanSkipBackward ) return;
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
          return state.PlayQueue[state.NowPlayingIndex] || {};
      },
      CanSkipForward(state) {
          return state.NowPlayingIndex > state.PlayQueueLength - 1;
      },
      CanSkipBackward(state) {
        return state.NowPlayingIndex > 0;
      },
      PlayQueueLength(state) {
          return state.PlayQueue.length;
      }
  }
})

export default store;
