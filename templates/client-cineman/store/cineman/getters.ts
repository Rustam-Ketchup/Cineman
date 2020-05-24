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
    return state.searchResults;
  }
};

export default getters;
