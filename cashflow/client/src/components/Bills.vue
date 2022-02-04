<template>
  <div class='bills'>
    <div class='bill' v-for="bill in bills" :key="bill.id">
      <p>{{bill.name}}</p>
      <p :class="bill.amount < 0 ? 'negative' : 'positive'">${{Math.abs(bill.amount)}}</p>
      <button v-if="(bill.amount < 0)">Make payment</button>
      <button v-else>Collect</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Bills',
  props: ['bills']
};


</script>
