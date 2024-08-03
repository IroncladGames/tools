struct vs_input
{
	float3 position : POSITION;	
};

struct vs_output
{
	float4 position : SV_POSITION;
};

vs_output main(vs_input input)
{
    vs_output output;
    output.position = float4(0,0,0,0);
	return output;
}
