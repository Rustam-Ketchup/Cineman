const getters = {
  getFilms(state: any) {
    return state.films;
  },
  getFilmLoaded(state: any) {
    return state.filmLoaded;
  },
  getFilmSelected(state: any) {
    return state.selectedFilm
  },
  getFilmPlatforms(state: any) {
    return state.platforms;
  },
  getSearchResults(state: any) {
    if (state.searchResults && state.searchResults.length === 0) return [{
      title: 'Results not found',
    }];

    return state.searchResults;
  }
};

export default getters;
