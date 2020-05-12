<template>
  <div class="container cineman">
    <Search v-if="getFilmSelected === ''" />
    <div v-else class="cineman-result">
      <h1 class="cineman-result__title">You select film: "{{ getFilmSelected }}"</h1>
      <button class="cineman-button" @click="clearFilm">Clear search</button>

      <div class="cineman-wrapper">
        <div
          v-for="(post, index) in getFilmsResults"
          :key="index"
          class="blog__post post-preview"
        >
          <div class="post-thumbnail"></div>
          <div class="post-content">
            <h1>{{ post.title }}</h1>
            <p>{{ post.description }}</p>
            <p>{{ post.platform }}</p>
            <p>{{ post.price }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
  import {
    Component,
    Vue,
    Watch
  } from "nuxt-property-decorator";
  import { namespace } from "vuex-class";
  import Search from "~/components/Search.vue";

  const cinemanStore = namespace('cineman');

  @Component({
    components: {
      Search
    }
  })
  export default class IndexPage extends Vue {
    @cinemanStore.Action private clearFilm: any;
    @cinemanStore.Getter private getFilmSelected: any;
    @cinemanStore.Getter private getFilmsResults: any;

  }
</script>

<style lang="scss">
  .container {
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .cineman {
    &-result {
      width: 90%;
      &__title {
        font-size: 4rem;
      }
    }

    &-wrapper {
      margin-top: 2rem;
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      grid-gap: 2rem;
      width: 100%;

      @media screen and (max-width: 1360px) {
        grid-template-columns: 50% 50%;
      }
      @media screen and (max-width: 980px) {
        grid-template-columns: 100%;
        width: 90%;
      }
    }

    &__title {
      margin: 1rem 0;
    }

    &__button {
      font-size: 1.2rem;
      cursor: pointer;
    }

    &__post {
      padding: 1rem;
      border: 2px solid #7f828b;
      border-radius: 1rem;
    }

    &-button {
      padding: 1rem 2rem;
      margin: 2rem;
      border: 1px solid;
      font-size: 2rem;
    }
  }

  .title {
    font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
      'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    display: block;
    font-weight: 300;
    font-size: 100px;
    color: #35495e;
    letter-spacing: 1px;
  }

  .subtitle {
    font-weight: 300;
    font-size: 42px;
    color: #526488;
    word-spacing: 5px;
    padding-bottom: 15px;
  }

  .links {
    padding-top: 15px;
  }

  .post-preview {
    border: 1px solid #ccc;
    box-shadow: 0 2px 2px #ccc;
    background-color: white;
  }

  .post-thumbnail {
    width: 100%;
    height: 200px;
    background-position: center;
    background-size: cover;
    background-image: url("../assets/thumb.jpg");
  }

  .post-content {
    padding: 10px;
    text-align: center;
  }

  .post-bottom {
    display: flex;
    justify-content: space-around;

    &__button {
      text-align: center;
      padding: .5rem 1rem;
      border: 1px solid #897777;
    }
  }

  .post-like--liked {
    color: #873333;
    background-color: #F7F8FB;
    box-shadow: 0 0 7px 2px rgba(153,153,255,1);
  }
</style>
