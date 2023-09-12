<script>

let promise = getFilmes();

async function getFilmes() {
    //Faz uma request GET p/ o endpoint /filmes
    const res = await fetch(`http://localhost:8000/filme/avatar`);
    const text = await res.json();

    if (res.ok) {
        return text;
    } else {
        throw new Error(text);
    }
}

function handleClick() {
    promise = getFilmes();
}

</script>

<button on:click={handleClick}> get filmes </button>

{#await promise}
	<p>...waiting</p>
{:then filmes}

	<h1>Lista de Filmes</h1>
    {#each filmes as filme }
        <p>{filme.title}</p>        
    {/each}
    
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}



