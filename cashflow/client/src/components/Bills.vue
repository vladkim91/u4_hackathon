<template>
  <div class='bills'>
    <div class='bill' v-for="bill in bills" :key="bill.id">
      <p>{{bill.name}}</p>
      <p :class="bill.amount < 0 ? 'negative' : 'positive'">${{Math.abs(bill.amount)}}</p>
      <button @click="adjustBalance" :value="bill.amount" v-if="(bill.amount < 0)">Make payment</button>
      <button @click="adjustBalance" :value="bill.amount" v-else>Collect</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Bills',
  props: ['bills'],
  methods: {
    adjustBalance(e) {
      e.preventDefault()
      this.$emit('adjustBalance', parseInt(e.target.value))
    } 
  }
};


</script>
