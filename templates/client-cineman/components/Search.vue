<template>
  <div class="search">
    <i class="fas fa-search"></i>
    <label>
      <input
        type="text"
        class="search__input"
        placeholder="Найди где смотреть с нами"
        @input="startTyping = true"
        v-model="searchInput"
      >
    </label>
    <div v-if="startTyping" class="search__dropdown">
      <span
        class="search__variant"
        v-for="(variant, index) in searchedVariants"
        :key="index"
        @click="clickVariantFilm(variant)"
      >
        {{ variant }}
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

    private searchInput = '';
    private startTyping = false;

    private searchedVariants = [
      'Film1',
      'Film2',
      'Film3',
      'Film4',
    ];

    private clickVariantFilm(film: string) {
      this.selectingFilm(film);
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

    .fa-search {
      font-size: 9rem;
    }

    &__input {
      border: none;
      background-color: inherit;
      outline: none;
      font-size: 4rem;
      padding: 4rem;
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
    }
  }
</style>
