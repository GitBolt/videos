const createSolanaAccount = (payer: Keypair) => {
    const connection = Connection("https://api.devnet.solana.com")
    const newAccount = Keypair.generate();
    
    console.log("New Account Public Key: ", newAccount.publicKey);

    const ix = SystemProgram.createAccount({
        fromPubkey: payer.publicKey,
        newAccountPubKey: newAccount.publicKey,
        lamports: 100000,
        programId: SystemProgram.programId,
        space: 0
    })
    const tx = new Transaction().add(ix)
    await sendAndConfirmTransaction(
        connection,
        transaction
        [payer, newAccount]
    )
}