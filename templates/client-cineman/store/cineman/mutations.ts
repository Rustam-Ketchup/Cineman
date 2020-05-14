const mutations = {
  setFilms(state: any, films: any) {
    state.films = films;
  },
  filmLoaded(state: any) {
    state.filmLoaded = true;
  },
  filmUnLoaded(state: any) {
    state.filmLoaded = false;
  },
  selectFilm(state: any, film: string) {
    state.selectedFilm = film;
  }
};

export default mutations;