<script>

    let promise = getArtist();
    
    async function getArtist() {
        //Faz uma request GET p/ o endpoint /filmes
        const res = await fetch(`http://127.0.0.1:8000/ator/1100`);
        const text = await res.json();
    
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }
    
    function handleClick() {
        promise = getArtist();
    }
    
</script>
    
<button on:click={handleClick}> get artist </button>
    
{#await promise}
    <p>...waiting</p>
{:then artista}  
    <h1>Artista e Biografia</h1>    
    <h1>{artista.name}</h1>
    <p>{artista.biografia}</p>
    <img src="{artista.imagem}" alt="">
            
            
{:catch error}
    <p style="color: red">{error.message}</p>
{/await}