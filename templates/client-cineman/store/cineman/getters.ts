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
  getFilmsResults(state: any) {
    return state.results;
  }
};

export default getters;
