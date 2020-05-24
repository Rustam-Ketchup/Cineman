<template>
  <div class="search">
    <i class="fas fa-search"></i>
    <input
      type="text"
      class="search__input"
      placeholder="Найди где смотреть с нами..."
      @input="onSearchInput($event.target.value)"
      v-model="searchInput"
    >
    <div v-if="startTyping" class="search__dropdown">
      <span
        class="search__variant"
        v-for="(variant, index) in getSearchResults"
        :key="index"
        @click="clickVariantFilm(variant)"
      >
        {{ variant.title }}
      </span>
    </div>
  </div>
</template>

<script lang="ts">
  import {
    Vue,
    Component
  } from "nuxt-property-decorator"
  import { namespace } from "vuex-class"

  const cinemanStore = namespace('cineman');

  @Component({
  })
  export default class Search extends Vue {
    @cinemanStore.Action private selectingFilm: any;
    @cinemanStore.Action private searchFilm: any;
    @cinemanStore.Getter private getSearchResults: any;

    private searchInput = '';
    private startTyping = false;

    private clickVariantFilm(film: any) {
      if (film && film.title) this.selectingFilm(film.title);
      else this.selectingFilm(film);
    }

    private onSearchInput(film: string) {
      if (this.searchInput === '') this.startTyping = false;

      else {
        this.startTyping = true;

        // start action search
        this.searchFilm(film);
      }
    }
  }
</script>

<style scoped lang="scss">
  .search {
    background-color: #F5F5F5;
    display: flex;
    align-items: center;
    justify-content: space-around;
    padding: .5rem 5rem;
    position: relative;
    width: 70%;

    .fa-search {
      font-size: 9rem;
    }

    &__input {
      border: none;
      background-color: inherit;
      outline: none;
      font-size: 4rem;
      font-style: italic;
      font-weight: 300;
      padding: 4rem;
      width: 100%;
      &::placeholder {
        font-weight: 300;
      }
    }

    &__dropdown {
      position: absolute;
      width: 100%;
      top: 100%;
      left: 0;
      padding: 1rem 2rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      background-color: #c3c3c3;
    }

    &__variant {
      cursor: pointer;
      padding: 1rem;
      font-size: 2.25rem;
      font-weight: 600;
      font-style: italic;
    }
  }
</style>
