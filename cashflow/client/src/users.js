export default [
  {
    pk: 1,
    username: 'vladkim',
    password: '123',
    email: 'vladkim123@mail.com',
    first_name: 'Vlad',
    last_name: 'Kim',
    balance: 1000,
    bills: [
      {
        name: 'Rent',
        amount: -1200,
        date: new Date()
      },
      {
        name: 'Salary',
        amount: 2000,
        date: new Date()
      },
      {
        name: 'Dividends',
        amount: 100,
        date: new Date()
      },
      {
        name: 'Internet',
        amount: -60,

        date: new Date()
      }
    ],
    transactions: [
      {
        name: 'Internet',
        amount: -60,
        date: new Date()
      },
      {
        name: 'Rent',
        amount: -1200,
        date: new Date()
      },

      {
        name: 'Salary',
        amount: 2200,
        date: new Date()
      }
    ]
  }
];
