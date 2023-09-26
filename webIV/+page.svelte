<script>
    let menu = 1;
    import Movie from "./Movie.svelte";
    import Nav from "./Nav.svelte";
    import Artist from "./Artist.svelte";
</script>

<Nav bind:menu/>

<div class="card">
	{#if menu === 1}
		<Movie/>
	{:else if menu === 2}
		<Artist/>
	{:else if menu === 3}
		OPTION 3
	{:else}
		OPTION 4
	{/if}
</div>