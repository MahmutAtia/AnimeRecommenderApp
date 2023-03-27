import { createSlice } from "@reduxjs/toolkit";

const urlSlice = createSlice({
  name: "url",
  initialState: "mahmoud",
  reducers: {
    search: (state, action) => ( state + action.payload)
    ,

    addmamo: (state) => (state + "mamo")
    ,
  },
});

export default urlSlice.reducer;
export const { search, addmamo } = urlSlice.actions;
