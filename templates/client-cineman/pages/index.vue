<template>
  <div class="container cineman">
    <h1 class="cineman__title">cineman</h1>
  </div>
</template>

<script lang="ts">
  import {
    Component,
    Vue,
    Watch
  } from "nuxt-property-decorator";
  import { namespace } from "vuex-class";

  const cinemanStore = namespace('cineman');

  @Component({
  })
  export default class IndexPage extends Vue {
    @cinemanStore.Action private loadFilms: any;

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
    &-wrapper {
      display: grid;
      grid-template-columns: 33% 33% 33%;
      grid-gap: 1rem;
      width: 60%;

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
