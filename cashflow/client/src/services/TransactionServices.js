import Client from './';

export const createTransaction = async (userId, name, amount, date) => {
  const result = await Client.post('/profile/transactions/create', {
    userId,
    name,
    amount,
    date
  });

  return result.data;
};
