<template>
  <div class="bills">
    <button @click="toggleEditing">
      {{ isEditing ? 'Stop Editing' : 'Edit' }}
    </button>
    <button @click="createBill">+</button>
    <div v-if="!isEditing">
      <table class="bill" v-for="(bill, index) in bills" :key="bill.id">
        <tr class="b-t-row">
          <td class="b-t-r-name-amount">
            <div class="b-t-name">{{ bill.name }}</div>
            <div
              :class="
                bill.amount < 0 ? 'negative b-t-amount' : 'positive b-t-amount'
              "
            >
              ${{ Math.abs(bill.amount) }}
            </div>
          </td>

          <td v-if="bill.amount < 0" class="b-t-button">
            <button
              @click="(e) => adjustBalance(e, index)"
              :value="bill.amount"
            >
              Pay
            </button>
          </td>
          <td v-else class="b-t-button">
            <button
              @click="(e) => adjustBalance(e, index)"
              :value="bill.amount"
            >
              Collect
            </button>
          </td>
        </tr>
      </table>
    </div>
    <div v-else>
      <div class="bill" v-for="(bill, index) in bills" :key="bill.id">
        <input
          name="name"
          type="text"
          :value="bill.name"
          @change="(e) => updateBill(e, index)"
        />
        <input
          name="amount"
          type="number"
          :value="bill.amount"
          @change="(e) => updateBill(e, index)"
        />
        <button @click="deleteBill(index)">x</button>
      </div>
    </div>
  </div>

  <!-- <div class='bills'> -->

  <!-- 
        <p :class="bill.amount < 0 ? 'negative' : 'positive'">${{Math.abs(bill.amount)}}</p>
        <button @click="(e) => adjustBalance(e, index)" :value="bill.amount" v-if="(bill.amount < 0)">Make payment</button>
        <button @click="(e) => adjustBalance(e, index)" :value="bill.amount" v-else>Collect</button>
      </div>
    </div> -->
</template>

<script>
export default {
  name: 'Bills',
  props: ['bills'],
  data: () => ({
    isEditing: false
  }),
  methods: {
    createBill() {
      this.$emit('createBill');
      this.isEditing = true;
    },
    updateBill(e, billIndex) {
      const billProperty = e.target.name;
      const billValue = e.target.value;

      this.$emit('updateBill', billProperty, billValue, billIndex);
    },
    deleteBill(billIndex) {
      this.$emit('deleteBill', billIndex);
    },
    toggleEditing() {
      this.isEditing = !this.isEditing;
    },
    adjustBalance(e, billIndex) {
      e.preventDefault();
      this.$emit('adjustBalance', parseInt(e.target.value), billIndex);
    }
  }
};
</script>
