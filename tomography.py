 t=time.time()
 qst_circuit = state_tomography_circuits(qc,[0])
 job = qiskit.execute(qst_circuit, Aer.get_backend('qasm_simulator'), shots=8000)
 tomo_circuit = StateTomographyFitter(job.result(), qst_circuit)
 rho_circuit = tomo_circuit.fit()