struct input
{
	float3 position : POSITION;	
};

float4 main(input input) : SV_TARGET 
{
	return float4(0,0,0,0);
}
