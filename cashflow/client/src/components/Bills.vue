<template>
  <div class='bills'>
    <button @click="toggleEditing">{{ isEditing ? 'Stop Editing' : 'Edit' }}</button>
    <div v-if="!isEditing">
      <div class='bill' v-for="bill in bills" :key="bill.id">
        <p>{{bill.name}}</p>
        <p :class="bill.amount < 0 ? 'negative' : 'positive'">${{Math.abs(bill.amount)}}</p>
        <button @click="adjustBalance" :value="bill.amount" v-if="(bill.amount < 0)">Make payment</button>
        <button @click="adjustBalance" :value="bill.amount" v-else>Collect</button>
      </div>
    </div>
    <div v-else>
      <div class='bill' v-for="(bill, index) in bills" :key="bill.id">
        <input name="name" type="text" :value="bill.name" @change="(e) => updateBill(e, index)">
        <input name="amount" type="number" :value="bill.amount" @change="(e) => updateBill(e, index)">
        <button @click="deleteBill(index)">x</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Bills',
  props: ['bills'],
  data: () => ({
    isEditing: false
  }),
  methods: {
    updateBill(e, billIndex) {
      const billProperty = e.target.name;
      const billValue = e.target.value;

      this.$emit('updateBill', billProperty, billValue, billIndex)
    },
    deleteBill(billIndex) {
      this.$emit('deleteBill', billIndex)
    },
    toggleEditing() {
      this.isEditing = !this.isEditing
    },
    adjustBalance(e) {
      e.preventDefault()
      this.$emit('adjustBalance', parseInt(e.target.value))
    } 
  }
};


</script>
