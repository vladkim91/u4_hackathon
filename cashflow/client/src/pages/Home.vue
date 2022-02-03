<template>
  <div class="home">
    
    <Bills />
    <Expenses />
    <Cashflow />
    
  </div>
</template>

<script>
import Bills from '../components/Bills.vue'
import Cashflow from '../components/Cashflow.vue';
import Expenses from '../components/Expenses.vue'

export default {

  name: 'Home',
  components: {
Bills,
Expenses,
    Cashflow
  }
};
</script>
