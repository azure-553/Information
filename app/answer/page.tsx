"use client";
import { useState } from "react";

import React from "react";

export default function Answer() {
  const [answer, setAnswer] = useState();
  return (
    <>
      <h1>answer</h1>
      <div>{answer}</div>
    </>
  );
}
