<template>
    <header class="header">
      <div class="header__content">

        <div class="header__block header__navigation">
          <n-link :to="'/'" class="anchor">Cineman</n-link>
        </div>

      </div>

    </header>
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
  export default class Header extends Vue {


  }
</script>

<style scoped lang="scss">
  .header {
    background-color: #f2f2f2;
    padding: 2px 0;
    position: sticky;
    top: 0;

    &__content {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      padding: 0 3rem;
    }
    &__block {
      padding: 1rem;
      font-size: 3rem;
      cursor: pointer;
    }
  }
</style>
