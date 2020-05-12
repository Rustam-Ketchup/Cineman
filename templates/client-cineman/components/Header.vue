<template>
    <header class="header">
      <div class="header__content">

        <div class="header__block header__navigation">
          <n-link :to="'/'" class="anchor"><i class="fas fa-home"></i> Home</n-link>
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
  import LoginForm from "~/components/LoginForm.vue";

  const cinemanStore = namespace('cineman');

  @Component({
  })
  export default class Header extends Vue {
    @cinemanStore.Getter private getUser: any;

    private showPopup: boolean = false;

    private openPopup() {
      this.showPopup = true
    }

    private closePopup() {
      this.showPopup = false
    }
  }
</script>

<style scoped lang="scss">
  .header {
    background-color: #f2f2f2;
    padding: 5px 0;
    position: sticky;
    top: 0;

    &__content {
      display: flex;
      align-items: center;
      justify-content: space-around;
    }
    &__block {
      padding: 1rem;
      border: 1px solid #333333;
      cursor: pointer;
    }
  }
</style>
