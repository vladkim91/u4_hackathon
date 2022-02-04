import Client from './';

export const createBill = async (userId) => {
  const result = await Client.post('/profile/bills/create', {
    id: userId
  });

  return result.data;
};

export const updateBill = async (billInfo) => {
  const result = await Client.put('/profile/bills/update', billInfo);

  return result.data;
};

export const deleteBill = async (id) => {
  const result = await Client.delete(`/profile/bills/${id}/delete`);

  return result.data;
};
