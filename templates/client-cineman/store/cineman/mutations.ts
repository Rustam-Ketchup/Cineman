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
  },
  setPlatforms(state: any, platforms: Array<any>) {
    state.platforms = platforms;
  },
  setSearchResults(state: any, results: Array<any>) {
    state.searchResults = results;
  },
  setLoading(state: any, loading: Boolean) {
    state.loading = loading;
  },

};

export default mutations;
